import os

html_content = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Medical Statistics & Health Research Hub | Dr. Suvinon</title>
  
  <!-- Tailwind CSS & Google Fonts -->
  <script src="https://cdn.tailwindcss.com"></script>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Sarabun:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
  
  <!-- KaTeX for Math Equations -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
  <script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js" onload="renderMathInElement(document.body);"></script>

  <style>
    body { font-family: 'Sarabun', sans-serif; }
    code, pre { font-family: 'JetBrains Mono', monospace; }
    .nav-active { border-left: 3px solid #2563eb; background: #eff6ff; color: #1d4ed8; font-weight: 600; }
  </style>
</head>
<body class="bg-slate-50 text-slate-800 antialiased flex flex-col min-h-screen">

  <!-- Header -->
  <header class="sticky top-0 z-50 bg-white border-b border-slate-200 shadow-sm">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex justify-between items-center h-16">
      <div class="flex items-center space-x-3">
        <span class="bg-blue-600 text-white font-bold p-2 rounded-lg text-lg leading-none">📊</span>
        <div>
          <h1 class="text-lg font-bold text-slate-900 leading-tight">MedStats & Research Hub</h1>
          <p class="text-xs text-slate-500">คลังความรู้สถิติการแพทย์ • ระบาดวิทยา • STATA Guideline</p>
        </div>
      </div>
      <div class="flex items-center space-x-3">
        <span class="text-xs font-medium px-2.5 py-1 bg-blue-50 text-blue-700 rounded-full border border-blue-200">Suvinon, M.D.</span>
        <a href="https://github.com/suvinonpl" target="_blank" class="text-slate-500 hover:text-slate-900 text-sm flex items-center gap-1">
          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24"><path fill-rule="evenodd" d="M12 2C6.477 2 2 6.484 2 12.017c0 4.425 2.865 8.18 6.839 9.504.5.092.682-.217.682-.483 0-.237-.008-.868-.013-1.703-2.782.605-3.369-1.343-3.369-1.343-.454-1.158-1.11-1.466-1.11-1.466-.908-.62.069-.608.069-.608 1.003.07 1.53 1.032 1.53 1.032.892 1.53 2.341 1.088 2.91.832.092-.647.35-1.088.636-1.338-2.22-.253-4.555-1.113-4.555-4.951 0-1.093.39-1.988 1.029-2.688-.103-.253-.446-1.272.098-2.65 0 0 .84-.27 2.75 1.026A9.564 9.564 0 0112 6.844c.85.004 1.705.115 2.504.337 1.909-1.296 2.747-1.027 2.747-1.027.546 1.379.202 2.398.1 2.651.64.7 1.028 1.595 1.028 2.688 0 3.848-2.339 4.695-4.566 4.943.359.309.678.92.678 1.855 0 1.338-.012 2.419-.012 2.747 0 .268.18.58.688.482A10.019 10.019 0 0022 12.017C22 6.484 17.522 2 12 2z" clip-rule="evenodd"></path></svg>
        </a>
      </div>
    </div>
  </header>

  <!-- Container -->
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 flex-1 w-full grid grid-cols-1 lg:grid-cols-4 gap-8">
    
    <!-- Sidebar Navigation -->
    <aside class="lg:col-span-1">
      <div class="sticky top-24 bg-white p-4 rounded-xl border border-slate-200 shadow-sm space-y-2">
        <h2 class="text-xs font-bold text-slate-400 uppercase tracking-wider px-3 pb-2 border-b border-slate-100">สารบัญหัวข้อ</h2>
        <nav class="space-y-1 text-sm">
          <a href="#anova-vs-ttest" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">1. ANOVA vs. t-test (F = t²)</a>
          <a href="#f-vs-t-dist" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">2. ทำไม F เบ้ขวา แต่ t สมมาตร?</a>
          <a href="#bartlett-rule" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">3. Bartlett's Test & Kruskal-Wallis</a>
          <a href="#ci-difference-vs-ratio" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">4. 95% CI คร่อม 0 vs. คร่อม 1</a>
          <a href="#why-dummy-i" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">5. การใช้ Dummy & ทำไมต้องใส่ i.</a>
          <a href="#regression-interpretation" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">6. การแปลผล Multiple Regression</a>
          <a href="#r-squared" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">7. R-squared vs. Adjusted R²</a>
          <a href="#logistic-interpretation" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">8. Logistic Regression (lbw)</a>
          <a href="#reg-vs-logistic" class="block px-3 py-2 rounded-lg hover:bg-slate-50 text-slate-700 transition">9. reg vs. logistic ใน STATA</a>
        </nav>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="lg:col-span-3 space-y-10">

      <!-- Hero Welcome -->
      <div class="bg-gradient-to-r from-blue-600 to-indigo-700 text-white p-6 rounded-2xl shadow-md">
        <h2 class="text-2xl font-bold mb-2">สรุปแก่นสถิติการแพทย์และการแปลผล STATA</h2>
        <p class="text-blue-100 text-sm leading-relaxed">
          รวบรวมหลักคิด ทฤษฎีสำคัญ การตั้งสมมติฐาน และประโยคแปลผลมาตรฐานสำหรับการสอบและตีพิมพ์งานวิจัย (อิงตามหลักสูตรปริญญาโท-เอก ภาควิชาเวชศาสตร์ป้องกันและสังคม)
        </p>
      </div>

      <!-- 1. ANOVA vs t-test -->
      <section id="anova-vs-ttest" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">01</span>
          <h3 class="text-lg font-bold text-slate-900">One-way ANOVA ใช้ใน 2 กลุ่มได้ไหม?</h3>
        </div>
        <p class="text-slate-600 mb-3 text-sm leading-relaxed">
          <strong>ใช้ได้ 100%</strong> ในทางคณิตศาสตร์สถิติ One-way ANOVA เมื่อใช้กับ 2 กลุ่ม จะให้ผลลัพธ์เทียบเท่ากับ <strong>Two-sample Independent t-test (two-tailed)</strong> พอดีเป๊ะ โดยมีความสัมพันธ์คือ:
        </p>
        <div class="bg-slate-50 p-4 rounded-lg border border-slate-200 text-center my-4 font-mono text-base text-blue-900 font-semibold">
          $$F = t^2 \quad \text{และ} \quad p\text{-value (ANOVA)} = p\text{-value (t-test two-tailed)}$$
        </div>
        <div class="text-xs bg-amber-50 text-amber-800 p-3 rounded-lg border border-amber-200">
          💡 <strong>ข้อแนะนำ:</strong> ถ้าเปรียบเทียบ 2 กลุ่ม นิยมรายงานเป็น t-test เพราะเห็นทิศทางผลต่างชัดเจน แต่ถ้า 3 กลุ่มขึ้นไป <em>ต้องใช้ One-way ANOVA</em> เพื่อคุมอัตราความคลาดเคลื่อนสะสม (Family-wise Error Rate)
        </div>
      </section>

      <!-- 2. F vs t distribution -->
      <section id="f-vs-t-dist" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">02</span>
          <h3 class="text-lg font-bold text-slate-900">ทำไมค่า F เป็นเบ้ขวาเสมอ แต่ค่า t เป็น Normal/สมมาตร?</h3>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4 text-sm">
          <div class="bg-blue-50/50 p-4 rounded-lg border border-blue-100">
            <h4 class="font-bold text-blue-900 mb-2">1) ค่าสถิติ t (วัดผลต่าง)</h4>
            <p class="text-xs text-slate-600 leading-relaxed mb-2">
              สูตรคือ \( t = \frac{\bar{X}_1 - \bar{X}_2}{SE} \) ตัวเศษเป็นผลต่างเชิงเส้น:
            </p>
            <ul class="text-xs text-slate-600 list-disc list-inside space-y-1">
              <li>กลุ่ม 1 > กลุ่ม 2 → ผลต่างเป็น <strong>บวก (+)</strong></li>
              <li>กลุ่ม 1 < กลุ่ม 2 → ผลต่างเป็น <strong>ลบ (-)</strong></li>
              <li>ศูนย์กลางใต้ \(H_0\) อยู่ที่ <strong>0</strong> กราฟจึงสมมาตรรูประฆังคว่ำ (-\(\infty\) ถึง +\(\infty\))</li>
            </ul>
          </div>
          <div class="bg-emerald-50/50 p-4 rounded-lg border border-emerald-100">
            <h4 class="font-bold text-emerald-900 mb-2">2) ค่าสถิติ F (วัดอัตราส่วนความแปรปรวน)</h4>
            <p class="text-xs text-slate-600 leading-relaxed mb-2">
              สูตรคือ \( F = \frac{MS_{\text{between}}}{MS_{\text{within}}} \) มาจากผลรวมกำลังสอง (Sum of Squares):
            </p>
            <ul class="text-xs text-slate-600 list-disc list-inside space-y-1">
              <li><strong>ไม่มีทางติดลบเด็ดขาด (\(F \ge 0\))</strong> เพราะเกิดจากตัวเลขยกกำลังสองหารกัน</li>
              <li>ศูนย์กลางใต้ \(H_0\) อยู่ใกล้ <strong>1</strong> (ความแปรปรวนพอๆ กัน)</li>
              <li>เมื่อกลุ่มต่างกันมาก ค่าจะพุ่งไปทางขวาเรื่อยๆ กราฟจึง <strong>เบ้ขวา (Right-skewed)</strong> เสมอ</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 3. Bartlett's Test -->
      <section id="bartlett-rule" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">03</span>
          <h3 class="text-lg font-bold text-slate-900">Bartlett's Test ตรวจอะไร & ทำไมต้องเปลี่ยนไปใช้ Kruskal-Wallis?</h3>
        </div>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">
          เวลาสั่ง <code>oneway y x</code> ใน STATA บรรทัดล่างสุดจะมี <strong>Bartlett's equal-variances test</strong> เสมอ เพื่อเช็คข้อตกลง Homoscedasticity (ความแปรปรวนทุกกลุ่มเท่ากันไหม):
        </p>
        <div class="overflow-x-auto text-sm">
          <table class="w-full border-collapse border border-slate-200">
            <thead class="bg-slate-100 text-slate-700 text-xs">
              <tr>
                <th class="border border-slate-200 p-2.5 text-left">ผลของ Bartlett's Test</th>
                <th class="border border-slate-200 p-2.5 text-left">ความหมายทางสถิติ</th>
                <th class="border border-slate-200 p-2.5 text-left">การดำเนินการวิเคราะห์</th>
              </tr>
            </thead>
            <tbody class="text-xs divide-y divide-slate-200">
              <tr class="bg-emerald-50/40">
                <td class="p-2.5 font-semibold text-emerald-800">Prob &gt; chi2 &ge; 0.05 (เช่น 0.721)</td>
                <td class="p-2.5 text-slate-700">ยอมรับ \(H_0\) → ความแปรปรวนของทุกกลุ่ม <strong>เท่ากัน (Equal variances)</strong></td>
                <td class="p-2.5 text-emerald-700 font-medium">✅ ผ่านเกณฑ์! อ่านผลตาราง One-way ANOVA ได้ตามปกติ</td>
              </tr>
              <tr class="bg-rose-50/40">
                <td class="p-2.5 font-semibold text-rose-800">Prob &gt; chi2 &lt; 0.05</td>
                <td class="p-2.5 text-slate-700">ปฏิเสธ \(H_0\) → ความแปรปรวนของแต่ละกลุ่ม <strong>ไม่เท่ากัน (Unequal)</strong></td>
                <td class="p-2.5 text-rose-700 font-medium">❌ ตกเกณฑ์! ถ้าข้อมูลเบ้มาก ให้เปลี่ยนไปใช้ <strong>Kruskal-Wallis test</strong> แทน</td>
              </tr>
            </tbody>
          </table>
        </div>
      </section>

      <!-- 4. 95% CI คร่อม 0 vs คร่อม 1 -->
      <section id="ci-difference-vs-ratio" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">04</span>
          <h3 class="text-lg font-bold text-slate-900">95% CI คร่อม 0 vs. คร่อม 1 ต่างกันอย่างไร?</h3>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-sm">
          <div class="border border-slate-200 rounded-lg p-4 bg-slate-50">
            <h4 class="font-bold text-slate-900 text-sm mb-1">1) 95% CI คร่อม 0 → วัด "ผลต่าง" (Difference)</h4>
            <p class="text-xs text-slate-600 mb-2">เกิดจากการนำค่า 2 กลุ่มมา <strong>ลบกัน (\(A - B\))</strong> เช่น Mean Diff, ค่า \(\beta\) ใน Linear Regression</p>
            <div class="text-xs space-y-1 bg-white p-2.5 rounded border border-slate-200">
              <p>• <strong>ค่า Null (\(H_0\)):</strong> คือ <strong>0</strong> (ถ้าเท่ากัน ลบกันต้องได้ 0)</p>
              <p>• <strong>ถ้าคร่อม 0 (เช่น [-0.02, 0.05]):</strong> ไม่ซิก (\(p \ge 0.05\))</p>
              <p>• <strong>ถ้าไม่คร่อม 0 (เช่น [0.01, 0.08]):</strong> ซิกอย่างมีนัยสำคัญ (\(p < 0.05\))</p>
            </div>
          </div>
          <div class="border border-slate-200 rounded-lg p-4 bg-slate-50">
            <h4 class="font-bold text-slate-900 text-sm mb-1">2) 95% CI คร่อม 1 → วัด "อัตราส่วน" (Ratio)</h4>
            <p class="text-xs text-slate-600 mb-2">เกิดจากการนำค่า 2 กลุ่มมา <strong>หารกัน (\(A / B\))</strong> เช่น Odds Ratio (OR), Relative Risk (RR), Hazard Ratio (HR)</p>
            <div class="text-xs space-y-1 bg-white p-2.5 rounded border border-slate-200">
              <p>• <strong>ค่า Null (\(H_0\)):</strong> คือ <strong>1</strong> (ถ้าเท่ากัน หารกันต้องได้ 1)</p>
              <p>• <strong>ถ้าคร่อม 1 (เช่น [0.75, 1.40]):</strong> ไม่ซิก (\(p \ge 0.05\))</p>
              <p>• <strong>ถ้าไม่คร่อม 1 (เช่น [1.20, 3.50]):</strong> ซิกอย่างมีนัยสำคัญ (\(p < 0.05\))</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 5. Dummy Variable & i. in Stata -->
      <section id="why-dummy-i" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">05</span>
          <h3 class="text-lg font-bold text-slate-900">การใช้ Dummy Variable & ทำไมต้องใส่ i. ใน STATA?</h3>
        </div>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">
          <strong>Dummy Variable</strong> คือการแปลงตัวแปรกลุ่มให้เป็นรหัส 0 กับ 1 เพื่อให้สมการคำนวณได้ โดยกฎทองคือ <strong>\(k - 1\)</strong> (มี \(k\) กลุ่ม สร้าง \(k-1\) ตัวแปรดัมมี่ เว้น 1 กลุ่มเป็น Reference)
        </p>
        <div class="bg-slate-900 text-slate-200 p-4 rounded-lg font-mono text-xs overflow-x-auto my-3">
          <p class="text-emerald-400"># ถ้าไม่ใส่ i. (STATA มองเป็นตัวเลขต่อเนื่องเส้นตรง)</p>
          <p>regress bwt race  <span class="text-slate-400">-> มองว่า race 1->2->3 เปลี่ยนแปลงเท่ากันเป็นเส้นตรง (ผิดหลักระบาดวิทยา!)</span></p>
          <br>
          <p class="text-emerald-400"># ถ้าใส่ i. (STATA แตกเป็น Dummy 0/1 ให้อัตโนมัติ)</p>
          <p>regress bwt i.race <span class="text-slate-400">-> เปรียบเทียบ Black vs. White และ Other vs. White ชัดเจน</span></p>
        </div>
      </section>

      <!-- 6. Multiple Linear Regression Interpretation -->
      <section id="regression-interpretation" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">06</span>
          <h3 class="text-lg font-bold text-slate-900">การแปลผลประโยคใน Multiple Linear Regression (ชุดข้อมูล lbw)</h3>
        </div>
        <div class="bg-slate-50 border-l-4 border-blue-600 p-3 mb-4 text-xs text-slate-700">
          คำสั่ง: <code>reg bwt i.race smoke age hyper wt_lmp</code> (ตัวแปรตาม bwt = น้ำหนักทารกแรกเกิด หน่วยกรัม)
        </div>
        <div class="space-y-3 text-xs leading-relaxed text-slate-700">
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-blue-900">• ตัวแปรกลุ่ม (race Black vs. White, coef = -495.15):</span>
            <p class="mt-1">"<strong>เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่</strong> ทารกที่เกิดจากมารดาเชื้อชาติ Black มีน้ำหนักแรกเกิดเฉลี่ย <em>น้อยกว่า</em> มารดาเชื้อชาติ White อยู่ <strong>495.15 กรัม</strong> อย่างมีนัยสำคัญทางสถิติ (95% CI: -800.75 ถึง -189.54, p = 0.002)"</p>
          </div>
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-blue-900">• ตัวแปรกลุ่ม 2 ระดับ (smoke, coef = -388.29):</span>
            <p class="mt-1">"<strong>เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่</strong> ทารกที่เกิดจากมารดาที่สูบบุหรี่ขณะตั้งครรภ์ มีน้ำหนักแรกเกิดเฉลี่ย <em>น้อยกว่า</em> มารดาที่ไม่สูบบุหรี่อยู่ <strong>388.29 กรัม</strong> อย่างมีนัยสำคัญทางสถิติ (95% CI: -600.85 ถึง -175.74, p < 0.001)"</p>
          </div>
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-blue-900">• ตัวแปรต่อเนื่อง (wt_lmp = นน.แม่, coef = +11.14):</span>
            <p class="mt-1">"<strong>เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่</strong> ทุกๆ 1 ปอนด์ที่เพิ่มขึ้นของน้ำหนักตัวมารดาก่อนตั้งครรภ์ สัมพันธ์กับน้ำหนักแรกเกิดของทารกที่ <strong>เพิ่มขึ้นเฉลี่ย 11.14 กรัม</strong> อย่างมีนัยสำคัญทางสถิติ (95% CI: 3.49 ถึง 18.80, p = 0.005)"</p>
          </div>
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-slate-700">• ตัวแปรไม่ซิก (age, coef = -3.13, p = 0.747):</span>
            <p class="mt-1">"เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่ ทุกๆ 1 ปีที่เพิ่มขึ้นของอายุมารดา สัมพันธ์กับน้ำหนักทารกที่ลดลงเฉลี่ย 3.13 กรัม <em>แต่ไม่พบความสัมพันธ์อย่างมีนัยสำคัญทางสถิติ</em> (95% CI: -22.24 ถึง 15.97, p = 0.747)"</p>
          </div>
        </div>
      </section>

      <!-- 7. R-squared -->
      <section id="r-squared" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">07</span>
          <h3 class="text-lg font-bold text-slate-900">R-squared vs. Adjusted R-squared ใน Regression คืออะไร?</h3>
        </div>
        <p class="text-sm text-slate-600 leading-relaxed mb-3">
          <strong>R² (Coefficient of Determination):</strong> คือ "สัดส่วนหรือร้อยละของความผันแปรของตัวแปรตาม (Y) ที่สามารถอธิบายได้ด้วยตัวแปรต้นทั้งหมดในโมเดล"
        </p>
        <div class="bg-slate-50 p-4 rounded-lg border border-slate-200 text-xs text-slate-700 space-y-2">
          <p>• <strong>ตัวอย่าง R² = 0.1774:</strong> "ตัวแปรต้นทั้งหมดร่วมกันอธิบายความผันแปรของน้ำหนักแรกเกิดทารกได้ <strong>17.74%</strong> (ส่วนอีก 82.26% เกิดจากปัจจัยอื่นที่ไม่ได้นำมาศึกษา)"</p>
          <p>• <strong>Adjusted R²:</strong> มีบทลงโทษ (Penalty) ตามจำนวนตัวแปรต้นที่ใส่ เพื่อป้องกันการใส่ตัวแปรที่ไม่มีประโยชน์แล้วทำให้ R² สูงหลอกตา นิยมใช้ตัวนี้ในการเปรียบเทียบโมเดล</p>
        </div>
      </section>

      <!-- 8. Logistic Regression Interpretation -->
      <section id="logistic-interpretation" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">08</span>
          <h3 class="text-lg font-bold text-slate-900">การแปลผล Multivariable Logistic Regression (Outcome = lbw: 0/1)</h3>
        </div>
        <p class="text-xs text-slate-600 mb-3">เมื่อตัวแปรตามเป็นกลุ่ม 0/1 ผลลัพธ์จะรายงานเป็น <strong>Adjusted Odds Ratio (AOR)</strong>:</p>
        <div class="space-y-3 text-xs leading-relaxed text-slate-700">
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-indigo-900">• ปัจจัยสูบบุหรี่ (smoke, AOR = 2.79, 95% CI: 1.29 - 6.05, p = 0.009):</span>
            <p class="mt-1">"เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่ มารดาที่สูบบุหรี่มีโอกาส (Odds) คลอดทารกน้ำหนักน้อยเป็น <strong>2.79 เท่า</strong> ของมารดาที่ไม่สูบบุหรี่ อย่างมีนัยสำคัญทางสถิติ"</p>
          </div>
          <div class="p-3 bg-white border border-slate-200 rounded-lg">
            <span class="font-bold text-indigo-900">• ปัจจัยต่อเนื่อง (wt_lmp = นน.แม่, AOR = 0.965, 95% CI: 0.937 - 0.994, p = 0.018):</span>
            <p class="mt-1">"เมื่อควบคุมปัจจัยอื่นๆ ให้คงที่ <strong>ทุกๆ 1 ปอนด์ที่เพิ่มขึ้น</strong> ของน้ำหนักตัวมารดาก่อนตั้งครรภ์ ทำให้โอกาส (Odds) คลอดทารกน้ำหนักน้อย <strong>ลดลง 3.5%</strong> (AOR = 0.965) อย่างมีนัยสำคัญทางสถิติ"</p>
          </div>
        </div>
      </section>

      <!-- 9. reg vs logistic in Stata -->
      <section id="reg-vs-logistic" class="bg-white p-6 rounded-xl border border-slate-200 shadow-sm scroll-mt-24">
        <div class="flex items-center gap-2 border-b border-slate-100 pb-3 mb-4">
          <span class="text-blue-600 font-bold text-lg">09</span>
          <h3 class="text-lg font-bold text-slate-900">reg vs. logistic ใน STATA คือคำสั่งเดียวกันไหม?</h3>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
            <span class="font-bold text-slate-900 text-sm">reg (Linear Regression)</span>
            <p class="mt-1 text-slate-600">• ตัวแปรตาม \(Y\) ต้องเป็น <strong>ตัวเลขต่อเนื่อง (Continuous)</strong> เช่น น้ำหนัก bwt, ความดัน</p>
            <p class="mt-1 text-slate-600">• รายงานผลเป็น <strong>Coefficient (\(\beta\))</strong> หรือผลต่างเฉลี่ย</p>
          </div>
          <div class="p-3 bg-slate-50 border border-slate-200 rounded-lg">
            <span class="font-bold text-slate-900 text-sm">logistic (Logistic Regression)</span>
            <p class="mt-1 text-slate-600">• ตัวแปรตาม \(Y\) ต้องเป็น <strong>กลุ่ม 2 ค่า (Binary 0/1)</strong> เช่น เป็นโรค/ไม่เป็น, lbw 0/1</p>
            <p class="mt-1 text-slate-600">• รายงานผลเป็น <strong>Odds Ratio (OR)</strong> ทันที</p>
          </div>
        </div>
      </section>

    </main>
  </div>

  <!-- Footer -->
  <footer class="bg-white border-t border-slate-200 py-6 text-center text-xs text-slate-500 mt-12">
    <p>Medical Statistics & Epidemiology Knowledge Base • Dr. Suvinon Pluckwattanachai</p>
    <p class="mt-1">Hosted on GitHub Pages • Generated automatically</p>
  </footer>

</body>
</html>
"""

target_path = "/Users/suvinonpluckwattanachai/My Drive/ปอ โท/med-stats-hub/index.html"
with open(target_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"Successfully created index.html at {target_path}")

# Create README.md
readme_content = """# Medical Statistics & Health Research Knowledge Hub
Academic & Clinical Biostatistics notes, STATA interpretations, and research methodologies.

- **Author:** Suvinon Pluckwattanachai, M.D.
- **Website:** https://suvinonpl.github.io/med-stats-hub/
"""

with open("/Users/suvinonpluckwattanachai/My Drive/ปอ โท/med-stats-hub/README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

print("Created README.md")
