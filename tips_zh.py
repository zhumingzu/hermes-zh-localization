1|"""Random tips shown at CLI session start to help users discover features."""
     2|
     3|import random
     4|
     5|
     6|# ---------------------------------------------------------------------------
     7|# Tip corpus — one-liners covering slash commands, CLI flags, config,
     8|# keybindings, tools, gateway, skills, profiles, and workflow tricks.
     9|# ---------------------------------------------------------------------------
    10|
    11|TIPS = [
    12|    # --- Slash Commands ---
    "/background <提示> (/bg 或 /btw) 在独立会话中后台运行任务，当前会话不受影响。",
    "/branch 分叉当前会话，让你可以探索不同方向而不丢失进度。",
    "/compress 在对话变长时手动压缩上下文。",
    "/rollback 列出文件系统检查点 —— 将代理修改的文件恢复到任意之前状态。",
    "/rollback diff 2 预览自检查点 2 以来的变化，不实际恢复。",
    "/rollback 2 src/file.py 从特定检查点恢复单个文件。",
    '/title "我的项目" 为会话命名 —— 之后可用 /resume 或 hermes -c 恢复。',
    "/resume 从之前命名的会话处继续。",
    "/queue <提示> 将消息排队到下一轮，不中断当前轮次。",
    "/undo 从对话中移除最后一对用户/助手消息。",
    "/retry 重发你上一条消息 —— 当助手回复不够准确时很有用。",
    "/verbose 循环切换工具进度显示：关闭 → 新工具 → 全部 → 详细。",
    "/reasoning high 提高模型推理深度。/reasoning show 显示推理过程。",
    "/fast 切换优先处理以加快 API 响应（取决于提供商）。",
    "/yolo 跳过当前会话所有危险命令的审批提示。",
    "/model 允许你在会话中途切换模型 —— 试试 /model sonnet 或 /model gpt-5。",
    "/model --global 永久更改你的默认模型。",
    "/personality pirate 设置有趣的个性 —— 14 种内置选项，从 kawaii 到 shakespeare。",
    "/skin 更改 CLI 主题 —— 试试 ares、mono、slate、poseidon 或 charizard。",
    "/statusbar 切换显示模型、token、上下文填充率、费用和耗时的常驻状态栏。",
    "/tools disable browser 临时禁用当前会话的浏览器工具。",
    "/browser connect 通过 CDP 将浏览器工具连接到正在运行的 Chrome 实例。",
    "/plugins 列出已安装的插件及其状态。",
    "/cron 管理定时任务 —— 设置定期提示并投递到任何平台。",
    "/reload-mcp 无需重启即可热重载 MCP 服务器配置。",
    "/usage 显示 token 使用量、费用明细和会话时长。",
    "/insights 显示过去 30 天的使用分析。",
    "/paste 检测剪贴板中是否有图片并附加到下一条消息。",
    "/profile 显示当前激活的配置文件及其主目录。",
    "/config 快速查看当前配置。",
    "/stop 终止代理产生的所有正在运行的后台进程。",
    44|
    45|    # --- @ Context References ---
    "@file:path/to/file.py 将文件内容直接注入消息中。",
    "@file:main.py:10-50 仅注入文件的第 10-50 行。",
    "@folder:src/ 注入目录树列表。",
    "@diff 将未暂存的 git 更改注入消息。",
    "@staged 将已暂存的 git 更改注入消息（git diff --staged）。",
    "@git:5 注入最近 5 次提交及完整补丁。",
    "@url:https://example.com 抓取并注入网页内容。",
    "输入 @ 触发文件路径自动补全 —— 交互式导航到任何文件。",
    '组合多个引用："请审查 @file:main.py 和 @file:test.py 的一致性。"',
    55|
    56|    # --- Keybindings ---
    "Alt+Enter 插入换行以支持多行输入。（Windows Terminal 会拦截 Alt+Enter —— 请使用 Ctrl+Enter 代替。）",
    "Ctrl+C 中断代理。2 秒内双击可强制退出。",
    "Ctrl+Z 将 Hermes 挂起到后台 —— 在 shell 中运行 fg 恢复。",
    "Tab 接受自动建议的幽灵文本或自动补全斜杠命令。",
    "代理正在工作时输入新消息可以中断并重定向它。",
    "Alt+V 将剪贴板中的图片粘贴到对话中。",
    "粘贴 5 行以上会自动保存到文件并插入紧凑引用。",
    64|
    65|    # --- CLI Flags ---
    'hermes -c 恢复最近的 CLI 会话。hermes -c "项目名" 按标题恢复。',
    "hermes -w 创建隔离的 git 工作树 —— 非常适合并行代理工作流。",
    'hermes -w -q "修复 issue #42" 结合工作树隔离与一次性查询。',
    "hermes chat -t web,terminal 仅启用特定工具集进行专注会话。",
    "hermes chat -s github-pr-workflow 在启动时预加载技能。",
    'hermes chat -q "查询" 运行单次非交互式查询后退出。',
    "hermes chat --max-turns 200 覆盖默认的每轮 90 次迭代限制。",
    "hermes chat --checkpoints 在每次破坏性文件更改前启用文件系统快照。",
    "hermes --yolo 跳过整个会话中所有危险命令的审批提示。",
    "hermes chat --source telegram 为会话打标签，方便在 hermes sessions list 中过滤。",
    "hermes -p work chat 使用特定配置文件运行，不更改默认配置。",
    77|
    78|    # --- CLI Subcommands ---
    "hermes doctor --fix 诊断并自动修复配置和依赖问题。",
    "hermes dump 输出紧凑的系统摘要 —— 提交 bug 报告时很有用。",
    "hermes config set KEY VALUE 自动将密钥路由到 .env，其余路由到 config.yaml。",
    "hermes config edit 用默认编辑器打开 config.yaml。",
    "hermes config check 扫描缺失或过时的配置项。",
    "hermes sessions browse 打开带搜索功能的交互式会话选择器。",
    "hermes sessions stats 按平台显示会话数量和数据库大小。",
    "hermes sessions prune --older-than 30 清理旧会话。",
    "hermes skills search react --source skills-sh 搜索 skills.sh 公开目录。",
    "hermes skills check 扫描已安装的 hub 技能是否有上游更新。",
    "hermes skills tap add myorg/skills-repo 添加自定义 GitHub 技能源。",
    "hermes skills snapshot export setup.json 导出技能配置用于备份或分享。",
    "hermes mcp add github --command npx 从命令行添加 MCP 服务器。",
    "hermes mcp serve 将 Hermes 本身作为 MCP 服务器运行，供其他代理使用。",
    "hermes auth add 允许添加多个 API 密钥进行凭证池轮换。",
    "hermes completion bash >> ~/.bashrc 为所有命令和配置文件启用 Tab 补全。",
    "hermes logs -f 实时跟踪 agent.log。--level WARNING --since 1h 过滤输出。",
    "hermes backup 创建整个 Hermes 主目录的 zip 备份。",
    "hermes profile create coder 创建隔离配置文件，自动成为独立命令。",
    "hermes profile create work --clone 将当前配置和密钥复制到新配置文件。",
    "hermes update 自动将新的内置技能同步到所有配置文件。",
    "hermes gateway install 将 Hermes 设置为系统服务（systemd/launchd）。",
    "hermes memory setup 配置外部记忆提供者（Honcho、Mem0 等）。",
    "hermes webhook subscribe 创建带 HMAC 验证的事件驱动 webhook 路由。",
    "省钱技巧：hermes tools 禁用不用的工具，hermes skills config 精简技能。",
    "/reasoning low 或 /reasoning minimal 将推理深度降到默认（medium）以下 —— 更快更便宜。",
    "hermes models 将视觉、压缩和辅助任务路由到更便宜的模型 —— 在不降低主聊天模型质量的情况下削减 85% 以上的后台 token 成本。",
   106|
   107|    # --- Configuration ---
    "在 config.yaml 中设置 display.bell_on_complete: true，长任务完成时响铃提醒。",
    "设置 display.streaming: true 可实时看到 token 逐个生成。",
    "设置 display.show_reasoning: true 可观察模型的思维链推理过程。",
    "设置 display.compact: true 减少输出中的空白，信息更密集。",
    "设置 display.busy_input_mode: queue 可在代理忙碌时将消息排队而非中断，或设为 steer 通过 /steer 中途注入。",
    "设置 display.resume_display: minimal 在恢复会话时跳过完整的对话回顾。",
    "设置 compression.threshold: 0.50 控制自动压缩触发的阈值（默认：上下文的 50%）。",
    "设置 agent.max_turns: 200 允许代理每轮进行更多工具调用步骤。",
    "设置 file_read_max_chars: 200000 增加 read_file 单次调用的最大内容量。",
    "设置 approvals.mode: smart 让 LLM 自动批准安全命令并拒绝危险命令。",
    "在 config.yaml 中设置 fallback_model，自动故障转移到备用提供商。",
    "设置 privacy.redact_pii: true 在发送给 LLM 之前哈希用户 ID 和电话号码。",
    "设置 browser.record_sessions: true 自动将浏览器会话录制为 WebM 视频。",
    "在 config.yaml 中设置 worktree: true 始终创建 git 工作树（等同于 hermes -w）。",
    "设置 security.website_blocklist.enabled: true 阻止 web 工具访问特定域名。",
    "设置 cron.wrap_response: false 投递原始代理输出，不带 cron 头部/尾部。",
    "HERMES_TIMEZONE 用任意 IANA 时区字符串覆盖服务器时区。",
    "config.yaml 支持环境变量替换：使用 ${VAR_NAME} 语法。",
    "config.yaml 中的 Quick commands 零 token 用量即可运行 shell 命令。",
    "可在 config.yaml 的 agent.personalities 下定义自定义个性。",
    "provider_routing 控制 OpenRouter 的提供商排序、白名单和黑名单。",
   129|
   130|    # --- Tools & Capabilities ---
    "execute_code 运行可编程调用 Hermes 工具的 Python 脚本 —— 结果不进入上下文。",
    "delegate_task 默认最多并行生成 3 个子代理（delegation.max_concurrent_children），各自拥有隔离上下文进行并行工作。",
    "web_extract 可用于 PDF URL —— 传入任意 PDF 链接即可转换为 markdown。",
    "search_files 基于 ripgrep，比 grep 快 —— 用它替代终端 grep。",
    "patch 使用 9 种模糊匹配策略，微小的空白差异不会导致编辑失败。",
    "patch 支持 V4A 格式进行批量多文件编辑，一次调用完成。",
    "read_file 在文件找不到时会建议相似文件名。",
    "read_file 自动去重 —— 重新读取未更改的文件返回轻量存根。",
    "browser_vision 截图后用 AI 分析 —— 适用于验证码和视觉内容。",
    "browser_console 可在页面上下文中执行 JavaScript 表达式。",
    "image_generate 使用 FLUX 2 Pro 创建图片并自动 2 倍放大。",
    "text_to_speech 将文本转换为语音 —— 在 Telegram 上以语音气泡形式播放。",
    "send_message 可在会话内触达任何已连接的消息平台。",
    "todo 工具帮助代理在会话期间跟踪复杂的多步骤任务。",
    "session_search 对所有历史对话进行全文搜索。",
    "代理会自动将偏好、纠正和环境信息保存到记忆中。",
    "mixture_of_agents 将难题路由到 4 个前沿 LLM 协作处理。",
    "终端命令支持后台模式，搭配 notify_on_complete 处理长时间任务。",
    "终端后台进程支持 watch_patterns，在特定输出行出现时提醒你。",
    "终端工具支持 6 种后端：本地、Docker、SSH、Modal、Daytona 和 Singularity。",
   151|
   152|    # --- Profiles ---
    "每个配置文件有自己独立的 config、API 密钥、记忆、会话、技能和 cron 任务。",
    "配置文件名称即 shell 命令 —— 'hermes profile create coder' 即创建 'coder' 命令。",
    "hermes profile export coder -o backup.tar.gz 创建便携式配置文件存档。",
    "如果两个配置文件意外共享同一 bot token，第二个网关会被阻止并显示明确错误。",
   157|
   158|    # --- Sessions ---
    "会话在首次对话后自动生成描述性标题 —— 无需手动命名。",
    '会话标题支持继承："我的项目" → "我的项目 #2" → "我的项目 #3"。',
    "退出时 Hermes 打印带会话 ID 和统计信息的恢复命令。",
    "hermes sessions export backup.jsonl 导出所有会话用于备份或分析。",
    "hermes -r SESSION_ID 通过 ID 恢复任意过往会话。",
   164|
   165|    # --- Memory ---
    "记忆是冻结快照 —— 更改仅在下一次会话启动时出现在系统提示中。",
    "记忆条目会自动扫描提示注入和数据外泄模式。",
    "代理有两个记忆存储：个人笔记（约 2200 字符）和用户档案（约 1375 字符）。",
    '你给代理的纠正（"不，应该这样做"）通常会被自动保存到记忆中。',
   170|
   171|    # --- Skills ---
    "超过 80 个内置技能，涵盖 GitHub、创意、MLOps、生产力、研究等领域。",
    "每个已安装的技能自动成为斜杠命令 —— 输入 / 查看全部。",
    "hermes skills install official/security/1password 安装仓库中的可选技能。",
    "技能可限制特定操作系统平台 —— 有些仅在 macOS 或 Linux 上加载。",
    "config.yaml 中的 skills.external_dirs 允许从自定义目录加载技能。",
    "代理可以使用 skill_manage 创建自己的技能作为程序性记忆。",
    "plan 技能将 markdown 计划保存到当前工作区的 .hermes/plans/ 下。",
   179|
   180|    # --- Cron & Scheduling ---
    'cron 任务可附加技能：hermes cron add --skill blogwatcher "检查新文章"。',
    "cron 投递目标包括 Telegram、Discord、Slack、邮件、短信等 12+ 个平台。",
   183|    "If a cron response starts with [SILENT], delivery is suppressed — useful for monitoring-only jobs.",
   184|    "Cron supports relative delays (30m), intervals (every 2h), cron expressions, and ISO timestamps.",
   185|    "Cron jobs run in completely fresh agent sessions — prompts must be self-contained.",
   186|
   187|    # --- Voice ---
   188|    "Voice mode works with zero API keys if faster-whisper is installed (free local speech-to-text).",
   189|    "Five TTS providers available: Edge TTS (free), ElevenLabs, OpenAI, NeuTTS (free local), MiniMax.",
   190|    "/voice on enables voice mode in the CLI. Ctrl+B toggles push-to-talk recording.",
   191|    "Streaming TTS plays sentences as they generate — you don't wait for the full response.",
   192|    "Voice messages on Telegram, Discord, WhatsApp, and Slack are auto-transcribed.",
   193|
   194|    # --- Gateway & Messaging ---
   195|    "Hermes runs on 21 messaging platforms: Telegram, Discord, Slack, WhatsApp, Signal, Matrix, IRC, Microsoft Teams, email, and more.",
   196|    "hermes gateway install sets it up as a system service that starts on boot.",
   197|    "DingTalk uses Stream Mode — no webhooks or public URL needed.",
   198|    "BlueBubbles brings iMessage to Hermes via a local macOS server.",
   199|    "Webhook routes support HMAC validation, rate limiting, and event filtering.",
   200|    "The API server exposes an OpenAI-compatible endpoint compatible with Open WebUI and LibreChat.",
   201|    "Discord voice channel mode: the bot joins VC, transcribes speech, and talks back.",
   202|    "group_sessions_per_user: true gives each person their own session in group chats.",
   203|    "/sethome marks a chat as the home channel for cron job deliveries.",
   204|    "The gateway supports inactivity-based timeouts — active agents can run indefinitely.",
   205|
   206|    # --- Security ---
   207|    "Dangerous command approval has 4 tiers: once, session, always (permanent allowlist), deny.",
   208|    "Smart approval mode uses an LLM to auto-approve safe commands and flag dangerous ones.",
   209|    "SSRF protection blocks private networks, loopback, link-local, and cloud metadata addresses.",
   210|    "Tirith pre-exec scanning detects homograph URL spoofing and pipe-to-interpreter patterns.",
   211|    "MCP subprocesses receive a filtered environment — only safe system vars pass through.",
   212|    "Context files (.hermes.md, AGENTS.md) are security-scanned for prompt injection before loading.",
   213|    "command_allowlist in config.yaml permanently approves specific shell command patterns.",
   214|
   215|    # --- Context & Compression ---
   216|    "Context auto-compresses when it reaches the threshold — memories are flushed and history summarized.",
   217|    "The status bar turns yellow, then orange, then red as context fills up.",
   218|    "SOUL.md at ~/.hermes/SOUL.md is the agent's primary identity — customize it to shape behavior.",
   219|    "Hermes loads project context from .hermes.md, AGENTS.md, CLAUDE.md, or .cursorrules (first match).",
   220|    "Subdirectory AGENTS.md files are discovered progressively as the agent navigates into folders.",
   221|    "Context files are capped at 20,000 characters with smart head/tail truncation.",
   222|
   223|    # --- Browser ---
   224|    "Five browser providers: local Chromium, Browserbase, Browser Use, Camofox, and Firecrawl.",
   225|    "Camofox is an anti-detection browser — Firefox fork with C++ fingerprint spoofing.",
   226|    "browser_navigate returns a page snapshot automatically — no need to call browser_snapshot after.",
   227|    "browser_vision with annotate=true overlays numbered labels on interactive elements.",
   228|
   229|    # --- MCP ---
   230|    "hermes mcp opens an interactive picker of Nous-approved MCPs you can install in one keystroke.",
   231|    "hermes mcp catalog lists Nous-approved MCP servers shipped with the repo.",
   232|    "hermes mcp install <name> installs a catalog entry, prompts for credentials, and lets you pick which of its tools to enable.",
   233|    "MCP servers are configured in config.yaml — both stdio and HTTP transports supported.",
   234|    "Per-server tool filtering: tools.include whitelists and tools.exclude blacklists specific tools.",
   235|    "MCP servers auto-generate toolsets at runtime — hermes tools can toggle them per platform.",
   236|    "MCP OAuth support: auth: oauth enables browser-based authorization with PKCE.",
   237|
   238|    # --- Checkpoints & Rollback ---
   239|    "Checkpoints have zero overhead when no files are modified — enabled by default.",
   240|    "A pre-rollback snapshot is saved automatically so you can undo the undo.",
   241|    "/rollback also undoes the conversation turn, so the agent doesn't remember rolled-back changes.",
   242|    "Checkpoints use shadow repos in ~/.hermes/checkpoints/ — your project's .git is never touched.",
   243|
   244|    # --- Batch & Data ---
   245|    "batch_runner.py processes hundreds of prompts in parallel for training data generation.",
   246|    "hermes chat -Q enables quiet mode for programmatic use — suppresses banner and spinner.",
   247|    "Trajectory saving (--save-trajectories) captures full tool-use traces for model training.",
   248|
   249|    # --- Plugins ---
   250|    "Three plugin types: general (tools/hooks), memory providers, and context engines.",
   251|    "hermes plugins install owner/repo installs plugins directly from GitHub.",
   252|    "8 external memory providers available: Honcho, OpenViking, Mem0, Hindsight, and more.",
   253|    "Plugin hooks include pre/post_tool_call, pre/post_llm_call, and transform_terminal_output for output canonicalization.",
   254|
   255|    # --- Miscellaneous ---
   256|    "Prompt caching (Anthropic) reduces costs by reusing cached system prompt prefixes.",
   257|    "The agent auto-generates session titles in a background thread — zero latency impact.",
   258|    "Smart model routing can auto-route simple queries to a cheaper model.",
   259|    "Slash commands support prefix matching: /h resolves to /help, /mod to /model.",
   260|    "Dragging a file path into the terminal auto-attaches images or sends as context.",
   261|    ".worktreeinclude in your repo root lists gitignored files to copy into worktrees.",
   262|    "hermes acp runs Hermes as an ACP server for VS Code, Zed, and JetBrains integration.",
   263|    "Custom providers: save named endpoints in config.yaml under custom_providers.",
   264|    "HERMES_EPHEMERAL_SYSTEM_PROMPT injects a system prompt that's never persisted to history.",
   265|    "credential_pool_strategies supports fill_first, round_robin, least_used, and random rotation.",
   266|    "hermes auth add nous or hermes auth add openai-codex sets up OAuth-based providers.",
   267|    "The API server supports both Chat Completions and Responses API with server-side state.",
   268|    "tool_preview_length: 0 in config shows full file paths in the spinner's activity feed.",
   269|    "hermes status --deep runs deeper diagnostic checks across all components.",
   270|
   271|    # --- Hidden Gems & Power-User Tricks ---
   272|    "Cron jobs can attach a Python script (--script) whose stdout is injected into the prompt as context.",
   273|    "Cron scripts live in ~/.hermes/scripts/ and run before the agent — perfect for data collection pipelines.",
   274|    "prefill_messages_file in config.yaml injects few-shot examples into every API call, never saved to history.",
   275|    "SOUL.md completely replaces the agent's default identity — rewrite it to make Hermes your own.",
   276|    "SOUL.md is auto-seeded with a default personality on first run. Edit ~/.hermes/SOUL.md to customize.",
   277|    "/compress <focus topic> allocates 60-70% of the summary budget to your topic and aggressively trims the rest.",
   278|    "On second+ compression, the compressor updates the previous summary instead of starting from scratch.",
   279|    "Before a gateway session reset, Hermes auto-flushes important facts to memory in the background.",
   280|    "network.force_ipv4: true in config.yaml fixes hangs on servers with broken IPv6 — monkey-patches socket.",
   281|    "The terminal tool annotates common exit codes: grep returning 1 = 'No matches found (not an error)'.",
   282|    "Failed foreground terminal commands auto-retry up to 3 times with exponential backoff (2s, 4s, 8s).",
   283|    "Bare sudo commands are auto-rewritten to pipe SUDO_PASSWORD from .env — no interactive prompt needed.",
   284|    "execute_code has built-in helpers: json_parse() for tolerant parsing, shell_quote(), and retry() with backoff.",
   285|    "execute_code's 7 sandbox tools (web_search, terminal, read/write/search/patch) use RPC — never enter context.",
   286|    "Reading the same file region 3+ times triggers a warning. At 4+, it's hard-blocked to prevent loops.",
   287|    "write_file and patch detect if a file was externally modified since the last read and warn about staleness.",
   288|    "V4A patch format supports Add File, Delete File, and Move File directives — not just Update.",
   289|    "MCP servers can request LLM completions back via sampling — the agent becomes a tool for the server.",
   290|    "MCP servers send notifications/tools/list_changed to trigger automatic tool re-registration without restart.",
   291|    "delegate_task with acp_command: 'claude' spawns Claude Code as a child agent from any platform.",
   292|    "Delegation has a heartbeat thread — child activity propagates to the parent, preventing gateway timeouts.",
   293|    "When a provider returns HTTP 402 (payment required), the auxiliary client auto-falls back to the next one.",
   294|    "agent.tool_use_enforcement steers models that describe actions instead of calling tools — auto for GPT/Codex.",
   295|    "agent.restart_drain_timeout (default 60s) lets running agents finish before a gateway restart takes effect.",
   296|    "agent.api_max_retries (default 3) controls how many times the agent retries a failed API call before surfacing the error — lower it for fast fallback.",
   297|    "The gateway caches AIAgent instances per session — destroying this cache breaks Anthropic prompt caching.",
   298|    "Any website can expose skills via /.well-known/skills/index.json — the skills hub discovers them automatically.",
   299|    "The skills audit log at ~/.hermes/skills/.hub/audit.log tracks every install and removal operation.",
   300|    "Stale git worktrees are auto-cleaned: 24-72h old with no unpushed commits get pruned on startup.",
   301|    "Each profile gets its own subprocess HOME at HERMES_HOME/home/ — isolated git, ssh, npm, gh configs.",
   302|    "HERMES_HOME_MODE env var (octal, e.g. 0701) sets custom directory permissions for web server traversal.",
   303|    "Container mode: place .container-mode in HERMES_HOME and the host CLI auto-execs into the container.",
   304|    "Ctrl+C has 5 priority tiers: cancel recording → cancel prompts → cancel picker → interrupt agent → exit.",
   305|    "Every interrupt during an agent run is logged to ~/.hermes/interrupt_debug.log with timestamps.",
   306|    "BROWSER_CDP_URL connects browser tools to any running Chromium-family browser — accepts WebSocket, HTTP, or host:port.",
   307|    "BROWSERBASE_ADVANCED_STEALTH=true enables advanced anti-detection with custom Chromium (Scale Plan).",
   308|    "The CLI auto-switches to compact mode in terminals narrower than 80 columns.",
   309|    "Quick commands support two types: exec (run shell command directly) and alias (redirect to another command).",
   310|    "Per-task delegation model: delegation.model and delegation.provider in config route subagents to cheaper models.",
   311|    "delegation.reasoning_effort independently controls thinking depth for subagents.",
   312|    "display.platforms in config.yaml allows per-platform display overrides: {telegram: {tool_progress: all}}.",
   313|    "human_delay.mode in config simulates human typing speed — configurable min_ms/max_ms range.",
   314|    "Config version migrations run automatically on load — new config keys appear without manual intervention.",
   315|    "GPT and Codex models get special system prompt guidance for tool discipline and mandatory tool use.",
   316|    "Gemini models get tailored directives for absolute paths, parallel tool calls, and non-interactive commands.",
   317|    "context.engine in config.yaml can be set to a plugin name for alternative context management strategies.",
   318|    "Browser pages over 8000 tokens are auto-summarized by the auxiliary LLM before returning to the agent.",
   319|    "The compressor does a cheap pre-pass: tool outputs over 200 chars are replaced with placeholders before the LLM runs.",
   320|    "When compression fails, further attempts are paused for 10 minutes to avoid API hammering.",
   321|    "Long dangerous commands (>70 chars) get a 'view' option in the approval prompt to see the full text first.",
   322|    "Audio level visualization shows ▁▂▃▄▅▆▇ bars during voice recording based on microphone RMS levels.",
   323|    "Profile names cannot collide with existing PATH binaries — 'hermes profile create ls' would be rejected.",
   324|    "hermes profile create backup --clone-all copies everything (config, keys, SOUL.md, memories, skills, sessions).",
   325|    "The voice record key is configurable via voice.record_key in config.yaml — not just Ctrl+B.",
   326|    ".cursorrules and .cursor/rules/*.mdc files are auto-detected and loaded as project context.",
   327|    "Context files support 10+ prompt injection patterns — invisible Unicode, 'ignore instructions', exfil attempts.",
   328|    "GPT-5 and Codex use 'developer' role instead of 'system' in the message format.",
   329|    "Per-task auxiliary overrides: auxiliary.vision.provider, auxiliary.compression.model, etc. in config.yaml.",
   330|    "The auxiliary client treats 'main' as a provider alias — resolves to your actual primary provider + model.",
   331|    "hermes claw migrate --dry-run previews OpenClaw migration without writing anything.",
   332|    "File paths pasted with quotes or escaped spaces are handled automatically — no manual cleanup needed.",
   333|    "Slash commands never trigger the large-paste collapse — /command with big arguments works correctly.",
   334|    "In interrupt mode, slash commands typed during agent execution bypass interrupt logic and run immediately.",
   335|    "HERMES_DEV=1 bypasses container mode detection for local development.",
   336|    "Each MCP server gets its own toolset (mcp-servername) that can be toggled independently via hermes tools.",
   337|    "MCP ${ENV_VAR} placeholders in config are resolved at server spawn — including vars from ~/.hermes/.env.",
   338|    "Skills from trusted repos (NousResearch) get a 'trusted' security level; community skills get extra scanning.",
   339|    "The skills quarantine at ~/.hermes/skills/.hub/quarantine/ holds skills pending security review.",
   340|
   341|    # --- Advanced Slash Commands ---
   342|    '/steer <prompt> injects a note after the next tool call — nudge direction mid-task without interrupting.',
   343|    '/goal <text> sets a standing Ralph-loop objective — Hermes auto-continues turn after turn until a judge says done.',
   344|    '/snapshot create [label] saves a full state snapshot of Hermes config; /snapshot restore <id> reverts later.',
   345|    '/copy [N] copies the last assistant response to your clipboard, or the Nth-from-last with a number.',
   346|    '/redraw forces a full UI repaint, fixing terminal drift after tmux resize or mouse selection artifacts.',
   347|    '/agents (alias /tasks) shows active agents and running background tasks across the current session.',
   348|    '/footer toggles the gateway footer on final replies showing model, tool counts, and turn timing.',
   349|    '/busy queue|steer|interrupt controls what pressing Enter does while Hermes is working.',
   350|    '/topic in Telegram DMs enables user-managed multi-session topic mode — /topic <id> restores past sessions inline.',
   351|    '/approve session|always runs a pending dangerous command with your chosen trust scope; /deny rejects it.',
   352|    '/restart gracefully restarts the gateway after draining active runs, then pings the requester when back up.',
   353|    '/kanban boards switch <slug> changes the active multi-project Kanban board from inside chat.',
   354|    '/reload reloads ~/.hermes/.env into the running session — pick up new API keys without restarting.',
   355|
   356|    # --- Cron (no-agent & scripts) ---
   357|    'cronjob with no_agent=True runs a script on schedule and sends its stdout directly — zero tokens, zero LLM.',
   358|    'An empty cron script stdout means silent tick — nothing is delivered, perfect for threshold watchdogs.',
   359|    "HERMES_CRON_MAX_PARALLEL (default 4) caps how many cron jobs run per tick so bursts don't saturate your keys.",
   360|
   361|    # --- Gateway Hooks ---
   362|    'Gateway hooks live under ~/.hermes/hooks/<name>/ with HOOK.yaml + handler.py — handler must be named `handle`.',
   363|    'Hook events include gateway:startup, session:start, agent:step, and command:* wildcard subscriptions.',
   364|    'Drop a ~/.hermes/BOOT.md checklist and a gateway:startup hook runs it as a one-shot agent every boot.',
   365|
   366|    # --- Curator ---
   367|    'hermes curator run --dry-run previews what the curator would archive or consolidate without mutating anything.',
   368|    "hermes curator pin <skill> hard-fences a skill against both auto-archival and the agent's skill_manage tool.",
   369|    'hermes curator rollback restores skills from a pre-run snapshot — backups live under skills/.curator_backups/.',
   370|
   371|    # --- Credential Pools & Routing ---
   372|    'hermes auth reset <provider> clears all cooldowns and exhaustion flags on a credential pool.',
   373|    'credential_pool_strategies.<provider>: round_robin cycles keys evenly instead of the fill_first default.',
   374|    'use_gateway: true per-tool routes web, image, tts, or browser through your Nous subscription — no extra keys.',
   375|    'provider_routing.data_collection: deny excludes data-storing providers on OpenRouter.',
   376|    'provider_routing.require_parameters: true only routes to providers that support every param in your request.',
   377|
   378|    # --- TUI & Dashboard ---
   379|    'HERMES_TUI_RESUME=1 auto-re-attaches to the most recent TUI session on launch — handy after SSH drops.',
   380|    "HERMES_TUI_THEME=light|dark|<hex> forces the TUI theme on terminals that don't set COLORFGBG.",
   381|    'Ctrl+G or Ctrl+X Ctrl+E in the TUI opens the input buffer in $EDITOR for long multi-line prompts.',
   382|    'The TUI renders LaTeX inline — $E=mc^2$ becomes Unicode math instead of raw TeX.',
   383|    'hermes dashboard launches a local web UI at 127.0.0.1:9119 — zero data leaves localhost.',
   384|    'hermes dashboard --tui embeds the full Hermes TUI in your browser via xterm.js and a WebSocket PTY.',
   385|    'Drop a YAML in ~/.hermes/dashboard-themes/ with two palette colors to reskin the entire dashboard.',
   386|    'Dashboard plugins are drop-in: manifest.json + JS bundle in ~/.hermes/dashboard-plugins/ — no npm build required.',
   387|    'layoutVariant: cockpit in a dashboard theme adds a 260px left rail that plugins can populate via the sidebar slot.',
   388|
   389|    # --- Env Vars & Config Gates ---
   390|    "display.tool_progress_command: true exposes /verbose on messaging platforms; it's CLI-only by default.",
   391|    'HERMES_BACKGROUND_NOTIFICATIONS=result only pings when background tasks finish (vs all/error/off).',
   392|    'HERMES_WRITE_SAFE_ROOT restricts write_file and patch to a directory prefix; writes outside require approval.',
   393|    'HERMES_IGNORE_RULES skips auto-injection of AGENTS.md, SOUL.md, .cursorrules, memory, and preloaded skills.',
   394|    'HERMES_ACCEPT_HOOKS auto-approves unseen shell hooks declared in config.yaml without a TTY prompt.',
   395|    'auxiliary.goal_judge.model routes the /goal judge to a cheap fast model to keep loop cost near zero.',
   396|    'Checkpoints skip directories with more than 50,000 files to avoid slow git operations on massive monorepos.',
   397|
   398|    # --- TTS ---
   399|    'tts.provider: piper runs 44-language local TTS on CPU — voices auto-download to ~/.hermes/cache/piper-voices/.',
   400|    'tts.providers.<name>.type: command wires any CLI TTS engine with {input_path} and {output_path} placeholders.',
   401|
   402|    # --- API Server & Proxy ---
   403|    'API_SERVER_ENABLED=true runs an OpenAI-compatible endpoint alongside the gateway for Open WebUI and LibreChat.',
   404|    'GATEWAY_PROXY_URL runs a split setup: platform I/O locally, agent work delegated to a remote API server.',
   405|
   406|    # --- Platform-specific ---
   407|    'MATRIX_DEVICE_ID pins a stable device ID for E2EE — without it, keys rotate every start and historic decrypt breaks.',
   408|    'TELEGRAM_WEBHOOK_SECRET is required whenever TELEGRAM_WEBHOOK_URL is set — generate with openssl rand -hex 32.',
   409|
   410|    # --- Batch ---
   411|    "batch_runner.py --resume content-matches completed prompts by text so dataset reorders don't re-run finished work.",
   412|
   413|    # --- Less-Known Slash Commands ---
   414|    '/new starts a fresh session in place (alias /reset) — fresh session ID, clean history, CLI stays open.',
   415|    '/clear wipes the terminal screen AND starts a new session — one shortcut for a visual reset.',
   416|    '/history prints the current conversation in-line without leaving the CLI — useful for a quick re-read.',
   417|    '/save writes the current conversation to disk without ending the session.',
   418|    '/status shows session info at a glance: ID, title, model, token usage, and elapsed time.',
   419|    '/image <path> attaches a local image file for your next prompt without pasting or drag-and-drop.',
   420|    '/platforms shows gateway and messaging-platform connection status right from inside chat.',
   421|    '/commands paginates the full slash-command + installed-skill list — useful on platforms without tab completion.',
   422|    '/toolsets lists every available toolset so you know what -t/--toolsets accepts.',
   423|    '/gquota shows Google Gemini Code Assist quota usage with progress bars when that provider is active.',
   424|    '/voice tts toggles TTS-only mode — agent replies out loud but you still type your prompts.',
   425|    '/reload-skills re-scans ~/.hermes/skills/ so drop-in skills appear without restarting the session.',
   426|    '/indicator kaomoji|emoji|unicode|ascii picks the TUI busy-indicator style shown during agent runs.',
   427|    '/debug uploads a support bundle (system info + logs) and returns shareable links — works in chat too.',
   428|
   429|    # --- CLI Subcommands & Flags ---
   430|    'hermes -z "<prompt>" is the purest one-shot: final answer on stdout, nothing else — ideal for piping in scripts.',
   431|    'hermes chat --pass-session-id injects the session ID into the system prompt so the agent can self-reference it.',
   432|    'hermes chat --image path/to/pic.png attaches a local image to a single -q query without a separate upload step.',
   433|    'hermes chat --ignore-user-config skips ~/.hermes/config.yaml — reproducible bug reports and CI runs.',
   434|    "hermes chat --source tool tags programmatic chats so they don't clutter hermes sessions list.",
   435|    'hermes dump --show-keys includes redacted API key fingerprints for deeper support debugging.',
   436|    'hermes sessions rename <ID> "new title" renames any past session; hermes sessions delete <ID> removes one.',
   437|    'hermes import restores a session export or profile archive produced by sessions export or profile export.',
   438|    'hermes fallback manages the fallback_model chain interactively — no hand-editing config.yaml.',
   439|    'hermes pairing rotates the DM pairing token — the first messager after rotation claims access to the bot.',
   440|    'hermes setup walks first-time users through provider, keys, and platform wiring in one interactive flow.',
   441|    'hermes status --deep runs the full health sweep across every component; plain hermes status is the quick view.',
   442|
   443|    # --- Agent Behavior Env Vars ---
   444|    'HERMES_AGENT_TIMEOUT=0 disables the gateway inactivity kill for a running agent — use for long research runs.',
   445|    'HERMES_ENABLE_PROJECT_PLUGINS=1 auto-loads repo-local plugins from ./.hermes/plugins/ — trust-gated by design.',
   446|    "HERMES_DISABLE_FILE_STATE_GUARD=1 turns off the 'file changed since you read it' guard on patch and write_file.",
   447|    'HERMES_ALLOW_PRIVATE_URLS=true lets web tools hit localhost and private networks — off by default in gateway mode.',
   448|    'HERMES_OPTIONAL_SKILLS=name1,name2 auto-installs extra optional-catalog skills on first run per profile.',
   449|    'HERMES_BUNDLED_SKILLS points at a custom bundled-skill tree — used by Homebrew and Nix packaging.',
   450|    'HERMES_DUMP_REQUEST_STDOUT=1 dumps every API request payload to stdout instead of log files.',
   451|    'HERMES_OAUTH_TRACE=*** logs redacted OAuth token exchange and refresh attempts for debugging provider auth.',
   452|    'HERMES_STREAM_RETRIES (default 3) controls mid-stream reconnect attempts on transient network errors.',
   453|
   454|    # --- Gateway Behavior Env Vars ---
   455|    'HERMES_GATEWAY_BUSY_ACK_ENABLED=false silences the ⚡/⏳/⏩ ack messages when a user messages a busy agent.',
   456|    'HERMES_AGENT_NOTIFY_INTERVAL (default 180s) sets how often the gateway pings with progress on long turns.',
   457|    'HERMES_RESTART_DRAIN_TIMEOUT (default 900s) caps how long /restart waits for in-flight runs before forcing.',
   458|    'HERMES_CHECKPOINT_TIMEOUT (default 30s) caps filesystem checkpoint creation — raise it on huge monorepos.',
   459|
   460|    # --- Auxiliary Tasks & Image Generation ---
   461|    'image_gen.model in config.yaml picks the FAL model: flux-2/klein, gpt-image-2, nano-banana-pro, and more.',
   462|    'image_gen.provider routes image generation through a plugin (OpenAI Images, Codex, FAL) instead of the default.',
   463|    'AUXILIARY_VISION_BASE_URL + AUXILIARY_VISION_API_KEY point vision analysis at any OpenAI-compatible endpoint.',
   464|
   465|    # --- Security ---
   466|    'security.tirith_fail_open: false makes Hermes block commands when the tirith scanner itself errors out.',
   467|    'TIRITH_FAIL_OPEN env var overrides the tirith_fail_open config — a quick toggle without editing config.yaml.',
   468|
   469|    # --- Sessions & Source Tags ---
   470|    '--source tool chats are excluded from hermes sessions list by default — set --source explicitly to see them.',
   471|    'Session IDs are timestamp-prefixed (20250305_091523_abcd) so sorting works naturally in ls and jq.',
   472|
   473|    # --- Misc ---
   474|    'API_SERVER_MODEL_NAME customizes the model name on /v1/models — essential for multi-profile Open WebUI setups.',
   475|    'Dashboard plugins are served from /dashboard-plugins/<name>/ — drop files into ~/.hermes/dashboard-plugins/.',
   476|]
   477|
   478|
   479|def get_random_tip(exclude_recent: int = 0) -> str:
   480|    """Return a random tip string.
   481|
   482|    Args:
   483|        exclude_recent: not used currently; reserved for future
   484|            deduplication across sessions.
   485|    """
   486|    return random.choice(TIPS)
   487|
   488|
   489|