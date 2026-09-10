(() => {
  "use strict";

  const state = {
    fileName: "",
    workbook: null,
    matrix: [],
    page: 0,
  };

  const ui = {
    fileInput: document.querySelector("#fileInput"),
    dropZone: document.querySelector("#dropZone"),
    fileSummary: document.querySelector("#fileSummary"),
    fileName: document.querySelector("#fileName"),
    rowCount: document.querySelector("#rowCount"),
    settings: document.querySelector("#settings"),
    sheetField: document.querySelector("#sheetField"),
    sheetSelect: document.querySelector("#sheetSelect"),
    headerRow: document.querySelector("#headerRow"),
    showHeaders: document.querySelector("#showHeaders"),
    hideEmpty: document.querySelector("#hideEmpty"),
    fitToPage: document.querySelector("#fitToPage"),
    downloadButton: document.querySelector("#downloadButton"),
    downloadLabel: document.querySelector("#downloadLabel"),
    errorMessage: document.querySelector("#errorMessage"),
    pager: document.querySelector("#pager"),
    previousPage: document.querySelector("#previousPage"),
    nextPage: document.querySelector("#nextPage"),
    currentPage: document.querySelector("#currentPage"),
    totalPages: document.querySelector("#totalPages"),
    emptyState: document.querySelector("#emptyState"),
    singlePreview: document.querySelector("#singlePreview"),
    pdfPages: document.querySelector("#pdfPages"),
  };

  function setError(message = "") {
    ui.errorMessage.textContent = message;
    ui.errorMessage.hidden = !message;
  }

  function cleanText(value) {
    if (value === null || value === undefined) return "";
    return String(value).replace(/\r\n?/g, "\n").trim();
  }

  function makeUniqueHeaders(row, width) {
    const used = new Map();
    return Array.from({ length: width }, (_, index) => {
      const base = cleanText(row[index]) || `未命名列 ${index + 1}`;
      const count = (used.get(base) || 0) + 1;
      used.set(base, count);
      return count === 1 ? base : `${base} (${count})`;
    });
  }

  function getParsedData() {
    const headerIndex = Math.max(0, Number(ui.headerRow.value || 1) - 1);
    if (!state.matrix.length || headerIndex >= state.matrix.length) return { headers: [], rows: [] };

    const width = Math.max(...state.matrix.map((row) => row.length), 0);
    const headers = makeUniqueHeaders(state.matrix[headerIndex] || [], width);
    const rows = state.matrix
      .slice(headerIndex + 1)
      .map((row, index) => ({ values: Array.from({ length: width }, (_, i) => cleanText(row[i])), sourceRow: headerIndex + index + 2 }))
      .filter(({ values }) => values.some(Boolean));
    return { headers, rows };
  }

  function activeOrientation() {
    return document.querySelector('input[name="orientation"]:checked').value;
  }

  function fieldList(headers, row) {
    return headers
      .map((label, index) => ({ label, value: row.values[index] || "" }))
      .filter((field) => !ui.hideEmpty.checked || field.value !== "");
  }

  function createPage(headers, row, pageIndex, total) {
    const orientation = activeOrientation();
    const fields = fieldList(headers, row);
    const page = document.createElement("article");
    page.className = `work-page ${orientation}`;

    const content = document.createElement("div");
    content.className = "page-content";

    const masthead = document.createElement("header");
    masthead.className = "page-masthead";
    const heading = document.createElement("div");
    const kicker = document.createElement("p");
    kicker.className = "page-kicker";
    kicker.textContent = "PRODUCTION WORK ORDER";
    const title = document.createElement("h3");
    title.className = "page-title";
    title.textContent = "生产工单";
    heading.append(kicker, title);

    const meta = document.createElement("div");
    meta.className = "page-meta";
    const fileLine = document.createElement("div");
    fileLine.textContent = state.fileName;
    const rowLine = document.createElement("div");
    rowLine.textContent = `原表第 ${row.sourceRow} 行 · 第 ${pageIndex + 1} / ${total} 页`;
    meta.append(fileLine, rowLine);
    masthead.append(heading, meta);

    const grid = document.createElement("div");
    grid.className = "page-grid";
    if (fields.length > (orientation === "landscape" ? 24 : 18)) grid.classList.add("dense");
    if (!ui.showHeaders.checked) grid.classList.add("no-headers");

    fields.forEach(({ label, value }) => {
      const cell = document.createElement("section");
      cell.className = "data-cell";
      const key = document.createElement("div");
      key.className = "data-label";
      key.textContent = label;
      const val = document.createElement("div");
      val.className = "data-value";
      val.textContent = value || "—";
      cell.append(key, val);
      grid.append(cell);
    });

    if (!fields.length) {
      const cell = document.createElement("section");
      cell.className = "data-cell";
      cell.textContent = "这一行没有可打印的数据";
      grid.append(cell);
    }

    const footer = document.createElement("footer");
    footer.className = "page-footer";
    const left = document.createElement("span");
    left.textContent = "操作人签名：________________";
    const right = document.createElement("span");
    right.textContent = "完成时间：________________";
    footer.append(left, right);
    content.append(masthead, grid, footer);
    page.append(content);
    return page;
  }

  function fitPage(page) {
    page.style.setProperty("--fit-scale", "1");
    if (!ui.fitToPage.checked) return;
    const content = page.querySelector(".page-content");
    const availableWidth = content.clientWidth;
    const availableHeight = content.clientHeight;
    const neededWidth = content.scrollWidth;
    const neededHeight = content.scrollHeight;
    const scale = Math.min(1, availableWidth / neededWidth, availableHeight / neededHeight);
    page.style.setProperty("--fit-scale", String(scale > 0 ? scale : 1));
  }

  function renderPreview() {
    setError();
    const { headers, rows } = getParsedData();
    const count = rows.length;
    state.page = Math.max(0, Math.min(state.page, count - 1));

    ui.rowCount.textContent = `${count} 页`;
    ui.totalPages.textContent = String(count || 1);
    ui.currentPage.textContent = String(count ? state.page + 1 : 1);
    ui.previousPage.disabled = state.page <= 0;
    ui.nextPage.disabled = state.page >= count - 1;
    ui.pager.hidden = count === 0;
    ui.emptyState.hidden = count > 0;
    ui.singlePreview.hidden = count === 0;
    ui.downloadButton.disabled = count === 0;
    ui.singlePreview.replaceChildren();

    if (count) {
      const page = createPage(headers, rows[state.page], state.page, count);
      ui.singlePreview.append(page);
      requestAnimationFrame(() => fitPage(page));
    }
  }

  function sheetToMatrix(sheet) {
    return window.XLSX.utils.sheet_to_json(sheet, {
      header: 1,
      defval: "",
      raw: false,
      blankrows: false,
    });
  }

  function selectSheet(name) {
    state.matrix = sheetToMatrix(state.workbook.Sheets[name]);
    state.page = 0;
    renderPreview();
  }

  async function readFile(file) {
    setError();
    if (!file) return;
    const extension = file.name.split(".").pop().toLowerCase();
    if (!window.XLSX) {
      setError("文件解析组件未加载，请检查网络连接后刷新页面。");
      return;
    }
    if (!['csv', 'xlsx'].includes(extension)) {
      setError("请选择 CSV 或 XLSX 文件。");
      return;
    }

    try {
      const buffer = await file.arrayBuffer();
      state.workbook = window.XLSX.read(buffer, { type: "array", cellDates: true });
      if (!state.workbook.SheetNames.length) throw new Error("没有找到工作表");
      state.fileName = file.name;
      ui.fileName.textContent = file.name;
      ui.fileSummary.hidden = false;
      ui.settings.disabled = false;
      ui.sheetSelect.replaceChildren();
      state.workbook.SheetNames.forEach((name) => {
        const option = document.createElement("option");
        option.value = name;
        option.textContent = name;
        ui.sheetSelect.append(option);
      });
      ui.sheetField.hidden = state.workbook.SheetNames.length < 2;
      selectSheet(state.workbook.SheetNames[0]);
    } catch (error) {
      console.error(error);
      setError("无法读取该文件。请确认文件未损坏，且格式为 CSV 或 XLSX。");
    } finally {
      ui.fileInput.value = "";
    }
  }

  async function downloadPdf() {
    const { headers, rows } = getParsedData();
    const PdfDocument = window.jspdf?.jsPDF;
    if (!rows.length || !window.html2canvas || !PdfDocument) {
      setError(rows.length ? "PDF 组件未加载，请检查网络连接后刷新页面。" : "没有可生成的工单数据。");
      return;
    }

    setError();
    ui.downloadButton.disabled = true;
    ui.downloadButton.classList.add("busy");
    ui.downloadLabel.textContent = "正在准备…";
    ui.pdfPages.replaceChildren(...rows.map((row, index) => createPage(headers, row, index, rows.length)));

    await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
    ui.pdfPages.querySelectorAll(".work-page").forEach(fitPage);

    const baseName = state.fileName.replace(/\.[^.]+$/, "") || "工单";
    const orientation = activeOrientation();
    try {
      const pdf = new PdfDocument({ unit: "mm", format: "a4", orientation, compress: true });
      const pages = [...ui.pdfPages.querySelectorAll(".work-page")];
      for (let index = 0; index < pages.length; index += 1) {
        ui.downloadLabel.textContent = `正在生成 ${index + 1} / ${pages.length}`;
        const canvas = await window.html2canvas(pages[index], {
          scale: 1.7,
          useCORS: true,
          backgroundColor: "#ffffff",
          logging: false,
        });
        if (index > 0) pdf.addPage("a4", orientation);
        const pageWidth = pdf.internal.pageSize.getWidth();
        const pageHeight = pdf.internal.pageSize.getHeight();
        pdf.addImage(canvas.toDataURL("image/jpeg", 0.94), "JPEG", 0, 0, pageWidth, pageHeight, undefined, "FAST");
        canvas.width = 1;
        canvas.height = 1;
      }
      pdf.save(`${baseName}-分页工单.pdf`);
    } catch (error) {
      console.error(error);
      setError("PDF 生成失败。可尝试切换纸张方向或打开“隐藏空字段”后重试。");
    } finally {
      ui.pdfPages.replaceChildren();
      ui.downloadButton.disabled = false;
      ui.downloadButton.classList.remove("busy");
      ui.downloadLabel.textContent = "生成 PDF";
    }
  }

  ui.fileInput.addEventListener("change", (event) => readFile(event.target.files[0]));
  ["dragenter", "dragover"].forEach((type) => ui.dropZone.addEventListener(type, (event) => {
    event.preventDefault();
    ui.dropZone.classList.add("dragging");
  }));
  ["dragleave", "drop"].forEach((type) => ui.dropZone.addEventListener(type, (event) => {
    event.preventDefault();
    ui.dropZone.classList.remove("dragging");
  }));
  ui.dropZone.addEventListener("drop", (event) => readFile(event.dataTransfer.files[0]));
  ui.sheetSelect.addEventListener("change", () => selectSheet(ui.sheetSelect.value));
  ui.previousPage.addEventListener("click", () => { state.page -= 1; renderPreview(); });
  ui.nextPage.addEventListener("click", () => { state.page += 1; renderPreview(); });
  ui.downloadButton.addEventListener("click", downloadPdf);
  ui.headerRow.addEventListener("input", () => { state.page = 0; renderPreview(); });
  [ui.showHeaders, ui.hideEmpty, ui.fitToPage].forEach((control) => control.addEventListener("change", renderPreview));
  document.querySelectorAll('input[name="orientation"]').forEach((control) => control.addEventListener("change", renderPreview));
})();
