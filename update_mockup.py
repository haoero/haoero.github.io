import re

with open('iron-condor-mockup-v2026-03-29-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Define the new Module 3 content
new_module_3 = """<!-- Module 3: 三套锦囊策略 A/B/C -->
        <div class="bg-gray-800 rounded-2xl p-8 shadow-md border border-gray-700 hover:border-gray-500 transition">
            <div class="flex items-center mb-6">
                <div class="bg-amber-900/50 p-3 rounded-lg mr-4">
                    <svg class="w-6 h-6 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"></path></svg>
                </div>
                <h2 class="text-2xl font-bold text-gray-100">三、铁鹰组合操作策略（锦囊A/B/C）</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <!-- A: 稳健型 -->
                <div class="border-2 border-emerald-800/80 rounded-2xl p-6 bg-gradient-to-b from-emerald-900/20 to-gray-800 relative overflow-hidden flex flex-col h-full shadow-[0_0_15px_rgba(16,185,129,0.1)]">
                    <div class="absolute top-0 right-0 bg-emerald-600/90 text-white text-xs font-bold px-3 py-1 rounded-bl-lg">主推方案</div>
                    <h3 class="text-xl font-bold text-emerald-400 mb-2">锦囊 A：稳健吃糖法</h3>
                    <p class="text-emerald-300/80 text-sm font-medium mb-4">远端宽翼，赚取高胜率权利金</p>
                    
                    <div class="space-y-4 flex-grow">
                        <!-- 1. 标的信息 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-emerald-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold flex justify-between items-center">
                                <span>1. 标的信息</span>
                                <span class="bg-gray-800 text-gray-300 px-2 py-0.5 rounded text-[10px] border border-gray-700">行权日: 260417</span>
                            </h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">Call 端 (看涨阻力)</span><span class="text-gray-200 font-mono text-xs">Sell 710 / Buy 720</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">Put 端 (看跌支撑)</span><span class="text-gray-200 font-mono text-xs">Sell 590 / Buy 580</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">当前价(净收权利金)</span>
                                    <span class="text-emerald-400 font-bold font-mono">$185.00</span>
                                </div>
                            </div>
                        </div>

                        <!-- 2. 资金核算 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-emerald-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold">2. 资金核算</h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">投入成本(初始)</span><span class="text-emerald-400/80 font-mono text-xs">+ $185.00</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">占用保证金</span><span class="text-gray-200 font-mono text-xs">$1,000.00</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">预期收益率</span>
                                    <span class="text-emerald-400 font-bold font-mono">18.50%</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3. 止损方案 -->
                        <div class="bg-emerald-950/30 rounded-xl p-4 border border-emerald-600/40 relative">
                            <div class="absolute -top-2 -left-2 flex h-4 w-4">
                              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-emerald-400 opacity-75"></span>
                              <span class="relative inline-flex rounded-full h-4 w-4 bg-emerald-500 border-2 border-gray-900"></span>
                            </div>
                            <h4 class="text-xs text-emerald-400 uppercase tracking-wider mb-2 font-semibold ml-2">3. 止损方案 (高亮)</h4>
                            <div class="text-xs text-gray-300 leading-relaxed space-y-2">
                                <p class="flex justify-between border-b border-emerald-900/50 pb-1">
                                    <span class="text-gray-400">防守底线：</span>
                                    <span>正股破 <strong class="text-red-400">595</strong> 或 <strong class="text-red-400">705</strong></span>
                                </p>
                                <div class="bg-black/40 p-2.5 rounded text-[11px] font-mono border border-emerald-800/50 text-emerald-100">
                                    <div class="text-emerald-500 mb-1 font-bold">【富途条件单配置】</div>
                                    <div class="flex justify-between"><span>条件类型:</span> <span class="text-gray-300">价格条件单</span></div>
                                    <div class="flex justify-between"><span>触发条件:</span> <span class="text-yellow-400">正股现价 ≤ 595 或 ≥ 705</span></div>
                                    <div class="flex justify-between"><span>订单类型:</span> <span class="text-gray-300">市价单买入平仓 Short 期权</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- B: 进取型 -->
                <div class="border-2 border-blue-800/80 rounded-2xl p-6 bg-gradient-to-b from-blue-900/20 to-gray-800 flex flex-col h-full shadow-[0_0_15px_rgba(59,130,246,0.05)] hover:border-blue-600 transition">
                    <h3 class="text-xl font-bold text-blue-400 mb-2">锦囊 B：进取收割法</h3>
                    <p class="text-blue-300/80 text-sm font-medium mb-4">贴近行权价，博取暴利差价</p>
                    
                    <div class="space-y-4 flex-grow">
                        <!-- 1. 标的信息 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-blue-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold flex justify-between items-center">
                                <span>1. 标的信息</span>
                                <span class="bg-gray-800 text-gray-300 px-2 py-0.5 rounded text-[10px] border border-gray-700">行权日: 260417</span>
                            </h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">Call 端</span><span class="text-gray-200 font-mono text-xs">Sell 690 / Buy 700</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">Put 端</span><span class="text-gray-200 font-mono text-xs">Sell 610 / Buy 600</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">当前价(净收)</span>
                                    <span class="text-blue-400 font-bold font-mono">$340.00</span>
                                </div>
                            </div>
                        </div>

                        <!-- 2. 资金核算 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-blue-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold">2. 资金核算</h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">投入成本</span><span class="text-blue-400/80 font-mono text-xs">+ $340.00</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">占用保证金</span><span class="text-gray-200 font-mono text-xs">$1,000.00</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">预期收益率</span>
                                    <span class="text-blue-400 font-bold font-mono">34.00%</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3. 止损方案 -->
                        <div class="bg-blue-950/30 rounded-xl p-4 border border-blue-600/40 relative">
                            <div class="absolute -top-2 -left-2 flex h-4 w-4">
                              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-blue-400 opacity-75"></span>
                              <span class="relative inline-flex rounded-full h-4 w-4 bg-blue-500 border-2 border-gray-900"></span>
                            </div>
                            <h4 class="text-xs text-blue-400 uppercase tracking-wider mb-2 font-semibold ml-2">3. 止损方案 (高亮)</h4>
                            <div class="text-xs text-gray-300 leading-relaxed space-y-2">
                                <p class="flex justify-between border-b border-blue-900/50 pb-1">
                                    <span class="text-gray-400">防守底线：</span>
                                    <span>正股破 <strong class="text-red-400">615</strong> 或 <strong class="text-red-400">685</strong></span>
                                </p>
                                <div class="bg-black/40 p-2.5 rounded text-[11px] font-mono border border-blue-800/50 text-blue-100">
                                    <div class="text-blue-500 mb-1 font-bold">【富途条件单配置】</div>
                                    <div class="flex justify-between"><span>条件类型:</span> <span class="text-gray-300">价格条件单</span></div>
                                    <div class="flex justify-between"><span>触发条件:</span> <span class="text-yellow-400">正股现价 ≤ 615 或 ≥ 685</span></div>
                                    <div class="flex justify-between"><span>订单类型:</span> <span class="text-gray-300">市价单买入平仓 Short 期权</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- C: 防御型 -->
                <div class="border-2 border-orange-800/80 rounded-2xl p-6 bg-gradient-to-b from-orange-900/20 to-gray-800 flex flex-col h-full shadow-[0_0_15px_rgba(249,115,22,0.05)] hover:border-orange-600 transition">
                    <h3 class="text-xl font-bold text-orange-400 mb-2">锦囊 C：防暴跌偏移法</h3>
                    <p class="text-orange-300/80 text-sm font-medium mb-4">不对称结构，重兵防御下行风险</p>
                    
                    <div class="space-y-4 flex-grow">
                        <!-- 1. 标的信息 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-orange-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold flex justify-between items-center">
                                <span>1. 标的信息</span>
                                <span class="bg-gray-800 text-gray-300 px-2 py-0.5 rounded text-[10px] border border-gray-700">行权日: 260417</span>
                            </h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">Call 端 (偏宽)</span><span class="text-gray-200 font-mono text-xs">Sell 700 / Buy 710</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">Put 端 (极宽)</span><span class="text-gray-200 font-mono text-xs">Sell 550 / Buy 540</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">当前价(净收)</span>
                                    <span class="text-orange-400 font-bold font-mono">$110.00</span>
                                </div>
                            </div>
                        </div>

                        <!-- 2. 资金核算 -->
                        <div class="bg-gray-900/60 rounded-xl p-4 border border-orange-800/30">
                            <h4 class="text-xs text-gray-400 uppercase tracking-wider mb-3 font-semibold">2. 资金核算</h4>
                            <div class="space-y-2 text-sm">
                                <div class="flex justify-between items-center"><span class="text-gray-500">投入成本</span><span class="text-orange-400/80 font-mono text-xs">+ $110.00</span></div>
                                <div class="flex justify-between items-center"><span class="text-gray-500">占用保证金</span><span class="text-gray-200 font-mono text-xs">$1,000.00</span></div>
                                <div class="flex justify-between items-center mt-2 pt-2 border-t border-gray-700/50">
                                    <span class="text-gray-400">预期收益率</span>
                                    <span class="text-orange-400 font-bold font-mono">11.00%</span>
                                </div>
                            </div>
                        </div>

                        <!-- 3. 止损方案 -->
                        <div class="bg-orange-950/30 rounded-xl p-4 border border-orange-600/40 relative">
                            <div class="absolute -top-2 -left-2 flex h-4 w-4">
                              <span class="animate-ping absolute inline-flex h-full w-full rounded-full bg-orange-400 opacity-75"></span>
                              <span class="relative inline-flex rounded-full h-4 w-4 bg-orange-500 border-2 border-gray-900"></span>
                            </div>
                            <h4 class="text-xs text-orange-400 uppercase tracking-wider mb-2 font-semibold ml-2">3. 止损方案 (高亮)</h4>
                            <div class="text-xs text-gray-300 leading-relaxed space-y-2">
                                <p class="flex justify-between border-b border-orange-900/50 pb-1">
                                    <span class="text-gray-400">防守底线：</span>
                                    <span>正股破 <strong class="text-red-400">555</strong> 或 <strong class="text-red-400">695</strong></span>
                                </p>
                                <div class="bg-black/40 p-2.5 rounded text-[11px] font-mono border border-orange-800/50 text-orange-100">
                                    <div class="text-orange-500 mb-1 font-bold">【富途条件单配置】</div>
                                    <div class="flex justify-between"><span>条件类型:</span> <span class="text-gray-300">价格条件单</span></div>
                                    <div class="flex justify-between"><span>触发条件:</span> <span class="text-yellow-400">正股现价 ≤ 555 或 ≥ 695</span></div>
                                    <div class="flex justify-between"><span>订单类型:</span> <span class="text-gray-300">市价单买入平仓 Short 期权</span></div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""

# Replace the old Module 3 using regex
# Look for the start of Module 3 comment and end of Module 3 div
pattern = r'<!-- Module 3: 三套锦囊策略 A/B/C -->.*?<!-- Module 4: 风控纪律 -->'
new_content = re.sub(pattern, new_module_3 + '\n\n        <!-- Module 4: 风控纪律 -->', content, flags=re.DOTALL)

with open('iron-condor-mockup-v2026-03-29-3.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("HTML updated!")
