(() => {
  "use strict";

  // Keys are normalized below so spaces, units, and duplicate-column suffixes
  // do not prevent a known field from receiving its translation.
  const myanmarFields = new Map([
    ["序号|序|编号|行号", "စဉ်"],
    ["客户|客户名称|客户名", "ဖောက်သည်"],
    ["订单|订单信息|客户订单信息", "အော်ဒါအချက်အလက်"],
    ["订单号|订单编号|客户订单号", "အော်ဒါနံပါတ်"],
    ["订单日期|下单日期|下单时间", "အော်ဒါရက်စွဲ"],
    ["交期|货期|交货日期|交货时间|交货期|交货日|交付日期|交付时间|交付期", "ပေးပို့ရမည့်ရက်"],
    ["日期|生产日期", "ရက်စွဲ"],
    ["品牌|商标", "အမှတ်တံဆိပ်"],
    ["印|印字|印刷|印刷内容|印字内容|印标|标识", "အမှတ်အသား"],
    ["圈|圈数|圈号|绕线圈数|绕线转数", "ကြိုးပတ်အပတ်ရေ"],
    ["围|周长|带周长|皮带周长|带长", "ပတ်လည်အလျား"],
    ["品名|产品名称|产品|名称", "ကုန်ပစ္စည်းအမည်"],
    ["货号|产品编号|产品货号|物料编号|物料编码", "ကုန်ပစ္စည်းနံပါတ်"],
    ["型号|产品型号|带型|型", "မော်ဒယ်"],
    ["号|号码", "နံပါတ်"],
    ["规格|产品规格", "သတ်မှတ်ချက်"],
    ["数量|订单数量|生产数量|条数", "အရေအတွက်"],
    ["单位", "ယူနစ်"],
    ["齿数|模具齿数|模齿数|楦块齿数", "သွားအရေအတွက်"],
    ["齿距|模具齿距|楦块齿距", "သွားအကွာအဝေး"],
    ["楦块|模具|模具编号", "ပုံစံခွက်"],
    ["模具长度|模长|楦块长度", "ပုံစံခွက်အလျား"],
    ["楦块齿高|模具齿高|齿高", "သွားအမြင့်"],
    ["楦块齿形|模具齿形|齿形", "သွားပုံစံ"],
    ["排线方向|绕线方向", "ကြိုးပတ်သည့်ဦးတည်ချက်"],
    ["绕线|排线", "ကြိုးပတ်ခြင်း"],
    ["长度|长|长度标记", "အလျား"],
    ["长度标准|长度基准|长度规格|标准长度|基准长度", "အလျားစံနှုန်း"],
    ["长度齿数", "အလျားသွားအရေအတွက်"],
    ["尺寸增量|尺寸增值|长度增量|长度增值|加长量|加长尺寸|增量", "အရွယ်အစားတိုးပမာဏ"],
    ["尺寸补偿|长度补偿|补偿尺寸|补偿值|补偿量", "အရွယ်အစားဖြည့်စွက်ပမာဏ"],
    ["尺寸加减|尺寸加减量|尺寸调整|长度加减|长度调整", "အရွယ်အစားညှိပမာဏ"],
    ["尺寸|成品尺寸|产品尺寸", "အရွယ်အစား"],
    ["宽度|宽|带宽", "အနံ"],
    ["厚度|胶厚", "အထူ"],
    ["线型|线号|线绳型号|线绳规格|线绳型|绳型号|绳芯型号|绳芯规格|线芯型号|棉绳型号|棉绳规格|绵绳型号|棉线型号|纱线型号", "ကြိုးအမျိုးအစား"],
    ["线长|线绳长度", "ကြိုးအလျား"],
    ["线数|线绳根数", "ကြိုးအရေအတွက်"],
    ["绕线长度", "ကြိုးပတ်အလျား"],
    ["绕线转速|转速", "လည်ပတ်နှုန်း"],
    ["覆胶|包胶", "ရော်ဘာဖုံးခြင်း"],
    ["包带|包布", "ပတ်တီးပတ်ခြင်း"],
    ["硫化", "ရော်ဘာအပူပေးခြင်း"],
    ["硫化温度|温度", "အပူချိန်"],
    ["硫化时间|时间", "အချိန်"],
    ["压力|硫化压力", "ဖိအား"],
    ["材料|材质|原料", "ကုန်ကြမ်း"],
    ["材料编号|材料编码|原料编号|原料编码", "ကုန်ကြမ်းနံပါတ်"],
    ["材料结构|材质结构|结构|线绳结构|线芯结构", "ကုန်ကြမ်းဖွဲ့စည်းပုံ"],
    ["颜色", "အရောင်"],
    ["备注|说明|特殊要求", "မှတ်ချက်"],
    ["负责人", "တာဝန်ခံ"],
    ["操作员|生产人员", "လုပ်သား"],
    ["检验员|质检员", "အရည်အသွေးစစ်ဆေးသူ"],
  ].flatMap(([aliases, translation]) => aliases.split("|").map((alias) => [alias, translation])));

  const signatureLabels = [
    ["绕线员签名", "ကြိုးပတ်သူ လက်မှတ်"],
    ["覆胶员签名", "ရော်ဘာဖုံးသူ လက်မှတ်"],
    ["包带员签名", "ပတ်တီးပတ်သူ လက်မှတ်"],
    ["硫化员签名", "ရော်ဘာအပူပေးသူ လက်မှတ်"],
    ["负责人签名", "တာဝန်ခံ လက်မှတ်"],
  ];

  const state = {
    fileName: "",
    workbook: null,
    matrix: [],
    page: 0,
    selectedColumns: new Set(),
    translations: new Map(),
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
    columnPicker: document.querySelector("#columnPicker"),
    columnList: document.querySelector("#columnList"),
    selectedColumnCount: document.querySelector("#selectedColumnCount"),
    selectAllColumns: document.querySelector("#selectAllColumns"),
    clearColumns: document.querySelector("#clearColumns"),
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

  function defaultTranslation(label) {
    const key = label.normalize("NFKC")
      .replace(/\s+/g, "")
      .replace(/[\[【]/g, "(").replace(/[\]】]/g, ")")
      .replace(/[：:]+$/g, "");
    if (myanmarFields.has(key)) return myanmarFields.get(key);

    // Spreadsheet exports append duplicate numbers and measurement units.
    // Keep meaningful qualifiers (such as 内径) instead of discarding them.
    const base = key
      .replace(/\((?:\d+|mm|cm|m|kg|g|pcs|rpm|mpa|℃|°c|毫米|厘米|米|条|个|圈|齿|秒|分钟|分|度|转\/分)\)/gi, "")
      .replace(/(?:[\/／](?:mm|cm|m|kg|g|pcs|rpm|mpa)|[\/／](?:毫米|厘米|米|条|个|圈|齿|秒|分钟|分|度|转\/分))$/gi, "");
    return myanmarFields.get(base) || "";
  }

  function bilingualLabel(element, chinese, myanmar) {
    element.append(document.createTextNode(chinese));
    if (myanmar) {
      const translation = document.createElement("span");
      translation.className = "myanmar-text";
      translation.lang = "my";
      translation.textContent = myanmar;
      element.append(translation);
    }
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
      .map((label, index) => ({ label, translation: state.translations.get(label) || "", value: row.values[index] || "" }))
      .filter((_, index) => state.selectedColumns.has(index))
      .filter((field) => !ui.hideEmpty.checked || field.value !== "");
  }

  function updateSelectedColumnCount(total) {
    ui.selectedColumnCount.textContent = `${state.selectedColumns.size} / ${total}`;
  }

  function renderColumnPicker(resetSelection = false) {
    const { headers } = getParsedData();
    if (resetSelection) state.selectedColumns = new Set(headers.map((_, index) => index));
    else state.selectedColumns = new Set([...state.selectedColumns].filter((index) => index < headers.length));

    ui.columnPicker.hidden = headers.length === 0;
    ui.columnList.replaceChildren();
    headers.forEach((header, index) => {
      if (!state.translations.has(header)) state.translations.set(header, defaultTranslation(header));
      const entry = document.createElement("div");
      entry.className = "column-entry";
      const option = document.createElement("label");
      option.className = "column-option";
      const checkbox = document.createElement("input");
      checkbox.type = "checkbox";
      checkbox.checked = state.selectedColumns.has(index);
      checkbox.dataset.columnIndex = String(index);
      const text = document.createElement("span");
      text.textContent = header;
      option.append(checkbox, text);
      const translation = document.createElement("input");
      translation.type = "text";
      translation.className = "column-translation";
      translation.lang = "my";
      translation.value = state.translations.get(header);
      translation.placeholder = "填写缅语翻译";
      translation.setAttribute("aria-label", `${header}的缅语翻译`);
      translation.addEventListener("input", () => {
        state.translations.set(header, translation.value.trim());
        renderPreview();
      });
      entry.append(option, translation);
      ui.columnList.append(entry);
    });
    updateSelectedColumnCount(headers.length);
  }

  function setAllColumns(selected) {
    const { headers } = getParsedData();
    state.selectedColumns = selected ? new Set(headers.map((_, index) => index)) : new Set();
    ui.columnList.querySelectorAll('input[type="checkbox"]').forEach((checkbox) => {
      checkbox.checked = selected;
    });
    updateSelectedColumnCount(headers.length);
    state.page = 0;
    renderPreview();
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
    kicker.lang = "my";
    kicker.textContent = "ထုတ်လုပ်မှုအလုပ်အမိန့်စာ";
    const title = document.createElement("h3");
    title.className = "page-title";
    title.textContent = "生产工单";
    heading.append(kicker, title);

    const meta = document.createElement("div");
    meta.className = "page-meta";
    const fileLine = document.createElement("div");
    fileLine.textContent = state.fileName;
    const rowLine = document.createElement("div");
    bilingualLabel(rowLine, `原表第 ${row.sourceRow} 行 · 第 ${pageIndex + 1} / ${total} 页`,
      `မူရင်းအတန်း ${row.sourceRow} · စာမျက်နှာ ${pageIndex + 1} / ${total}`);
    meta.append(fileLine, rowLine);
    masthead.append(heading, meta);

    const grid = document.createElement("div");
    grid.className = "page-grid";
    if (fields.length > (orientation === "landscape" ? 24 : 18)) grid.classList.add("dense");
    if (!ui.showHeaders.checked) grid.classList.add("no-headers");

    fields.forEach(({ label, translation, value }) => {
      const cell = document.createElement("section");
      cell.className = "data-cell";
      const key = document.createElement("div");
      key.className = "data-label";
      bilingualLabel(key, label, translation);
      const separator = document.createElement("span");
      separator.className = "data-separator";
      separator.textContent = "：";
      separator.setAttribute("aria-hidden", "true");
      const val = document.createElement("div");
      val.className = "data-value";
      val.textContent = value || "—";
      cell.append(key, separator, val);
      grid.append(cell);
    });

    if (!fields.length) {
      const cell = document.createElement("section");
      cell.className = "data-cell";
      bilingualLabel(cell, "这一行没有可打印的数据", "ပုံနှိပ်ရန် အချက်အလက်မရှိပါ");
      grid.append(cell);
    }

    const signatures = document.createElement("footer");
    signatures.className = "signature-grid";
    signatureLabels.forEach(([name, translation]) => {
      const signature = document.createElement("div");
      signature.className = "signature-item";
      const label = document.createElement("span");
      label.className = "signature-label";
      bilingualLabel(label, name, translation);
      const line = document.createElement("span");
      line.className = "signature-line";
      signature.append(label, line);
      signatures.append(signature);
    });
    content.append(masthead, grid, signatures);
    page.append(content);
    return page;
  }

  function fitPage(page) {
    page.style.setProperty("--fit-scale", "1");
    if (!ui.fitToPage.checked) return;
    const content = page.querySelector(".page-content");
    let scale = 1;
    // Scaling changes the available line width, so remeasure wrapped labels.
    for (let attempt = 0; attempt < 4; attempt += 1) {
      const ratio = Math.min(1, content.clientWidth / content.scrollWidth, content.clientHeight / content.scrollHeight);
      if (ratio >= 1) break;
      scale *= ratio;
      page.style.setProperty("--fit-scale", String(scale));
    }
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
    ui.downloadButton.disabled = count === 0 || state.selectedColumns.size === 0;
    ui.singlePreview.replaceChildren();

    if (count) {
      const page = createPage(headers, rows[state.page], state.page, count);
      ui.singlePreview.append(page);
      requestAnimationFrame(() => {
        fitPage(page);
        // Importing the first sheet can trigger the first use of this font.
        document.fonts.ready.then(() => {
          if (page.isConnected) fitPage(page);
        });
      });
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
    renderColumnPicker(true);
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

    const baseName = state.fileName.replace(/\.[^.]+$/, "") || "工单";
    const orientation = activeOrientation();
    try {
      await document.fonts.ready;
      await new Promise((resolve) => requestAnimationFrame(() => requestAnimationFrame(resolve)));
      ui.pdfPages.querySelectorAll(".work-page").forEach(fitPage);
      const pdf = new PdfDocument({ unit: "mm", format: "a5", orientation, compress: true });
      const pages = [...ui.pdfPages.querySelectorAll(".work-page")];
      for (let index = 0; index < pages.length; index += 1) {
        ui.downloadLabel.textContent = `正在生成 ${index + 1} / ${pages.length}`;
        const canvas = await window.html2canvas(pages[index], {
          scale: 1.7,
          useCORS: true,
          backgroundColor: "#ffffff",
          logging: false,
        });
        if (index > 0) pdf.addPage("a5", orientation);
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
      ui.downloadButton.disabled = rows.length === 0 || state.selectedColumns.size === 0;
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
  ui.columnList.addEventListener("change", (event) => {
    const checkbox = event.target.closest('input[type="checkbox"]');
    if (!checkbox) return;
    const index = Number(checkbox.dataset.columnIndex);
    if (checkbox.checked) state.selectedColumns.add(index);
    else state.selectedColumns.delete(index);
    updateSelectedColumnCount(getParsedData().headers.length);
    state.page = 0;
    renderPreview();
  });
  ui.selectAllColumns.addEventListener("click", () => setAllColumns(true));
  ui.clearColumns.addEventListener("click", () => setAllColumns(false));
  ui.previousPage.addEventListener("click", () => { state.page -= 1; renderPreview(); });
  ui.nextPage.addEventListener("click", () => { state.page += 1; renderPreview(); });
  ui.downloadButton.addEventListener("click", downloadPdf);
  ui.headerRow.addEventListener("input", () => {
    state.page = 0;
    renderColumnPicker(true);
    renderPreview();
  });
  [ui.showHeaders, ui.hideEmpty, ui.fitToPage].forEach((control) => control.addEventListener("change", renderPreview));
  document.querySelectorAll('input[name="orientation"]').forEach((control) => control.addEventListener("change", renderPreview));
})();
