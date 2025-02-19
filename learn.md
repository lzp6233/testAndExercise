

以下是Git基本指令的详细说明，涵盖仓库管理、文件操作、分支管理、远程协作等核心功能，并结合资料提供具体用法和示例：

---

### 一、仓库初始化与配置
1. **初始化仓库**  
   - `git init`：在当前目录创建本地仓库，生成`.git`子目录。  
示例：  
     ```bash
     mkdir my_project && cd my_project  
     git init  # 
     ```


2. **克隆远程仓库**  
   - `git clone <远程仓库URL> [本地目录名]`：将远程仓库完整复制到本地。  
示例：  
     ```bash
     git clone https://github.com/user/repo.git  # 
     ```


3. **配置用户信息**  
   - 全局配置：  
     ```bash
     git config --global user.name "Your Name"  
     git config --global user.email "email@example.com"  # 
     ```

   - 查看配置：`git config --list`  # 

---

### 二、文件操作与提交
1. **添加文件到暂存区**  
   - `git add <文件/目录>`：将指定文件或目录的修改添加到暂存区。  
- `git add .`：添加当前目录所有修改（新文件、修改、删除）。  
- `git add -A`：等效于`git add .`，覆盖所有变更。  
- `git add -u`：仅添加已跟踪文件的修改（不包括新文件）。  
示例：  
     ```bash
     git add index.html  # 
     git add src/  # 添加整个目录
     ```


2. **提交更改到本地仓库**  
   - `git commit -m "提交信息"`：提交暂存区的所有修改。  
- `git commit --amend`：修改最近一次提交的信息或内容。  
示例：  
     ```bash
     git commit -m "修复登录页面Bug"  # 
     git commit --amend -m "修正拼写错误"  # 
     ```


3. **查看仓库状态**  
   - `git status`：显示工作区、暂存区的文件状态。  
- `git status -s`：简洁模式输出（标记A表示新增，M表示修改，D表示删除）。  
示例输出：  
     ```
     M  README.md  # 修改未暂存  
     A  new_file.txt  # 新增已暂存  
     D  old_file.txt  # 删除未暂存  # 
     ```


---

### 三、提交历史与差异查看
1. **查看提交历史**  
   - `git log`：显示完整提交历史，包括作者、日期和提交信息。  
- `git log --oneline`：单行简略显示提交ID和说明。  
- `git log --graph`：图形化显示分支合并历史。  
- `git log --author="John"`：筛选特定作者的提交。  
示例：  
     ```bash
     git log --oneline --since="2024-01-01"  # 显示2024年后的提交  # 
     ```


2. **查看文件差异**  
   - `git diff`：比较工作区与暂存区的差异。  
   - `git diff --staged`：比较暂存区与最新提交的差异。  
示例：  
     ```bash
     git diff HEAD~2 HEAD  # 比较最近两次提交的差异  # 
     ```


---

### 四、分支管理
1. **创建与切换分支**  
   - `git branch <分支名>`：创建新分支。  
   - `git checkout <分支名>`或`git switch <分支名>`：切换分支。  
   - `git checkout -b <新分支名>`：创建并切换到新分支。  
示例：  
     ```bash
     git branch feature-login  
     git switch feature-login  # 
     ```


2. **合并分支**  
   - `git merge <分支名>`：将指定分支合并到当前分支。  
- 解决冲突：手动编辑冲突文件后执行`git add`和`git commit`。  
示例：  
     ```bash
     git switch main  
     git merge feature-login  # 
     ```


3. **删除分支**  
   - `git branch -d <分支名>`：删除已合并的分支。  
   - `git branch -D <分支名>`：强制删除未合并的分支。  
示例：  
     ```bash
     git branch -d old-feature  # 
     ```


---

### 五、远程仓库协作
1. **关联远程仓库**  
   - `git remote add <别名> <远程URL>`：添加远程仓库别名。  
   - `git remote -v`：查看已关联的远程仓库列表。  
示例：  
     ```bash
     git remote add origin https://github.com/user/repo.git  # 
     ```


2. **推送与拉取更新**  
   - `git push <远程别名> <分支名>`：推送本地分支到远程仓库。  
   - `git pull <远程别名> <分支名>`：拉取远程分支并合并到当前分支（等价于`git fetch` + `git merge`）。  
   - `git fetch`：仅获取远程更新但不自动合并。  
示例：  
     ```bash
     git push origin main  # 
     git pull origin dev  # 
     ```


---

### 六、高级操作
1. **暂存临时修改**  
   - `git stash`：保存工作区未提交的修改（适用于临时切换分支）。  
   - `git stash pop`：恢复最近一次暂存的修改并删除记录。  
示例：  
     ```bash
     git stash  # 保存当前修改  
     git stash list  # 查看暂存列表  
     git stash pop  # 
     ```


2. **标签管理**  
   - `git tag <标签名>`：为当前提交创建轻量标签。  
   - `git tag -a v1.0 -m "版本1.0"`：创建含注释的附注标签。  
   - `git push origin --tags`：推送所有标签到远程仓库。  
示例：  
     ```bash
     git tag v1.0  # 
     ```


3. **撤销与回滚**  
   - `git reset --hard HEAD^`：回退到上一个提交（慎用，会丢失未提交的修改）。  
   - `git revert <提交ID>`：创建新提交以撤销指定提交的更改（安全回滚）。  
示例：  
     ```bash
     git revert abc123  # 撤销提交abc123的更改  # 
     ```


---

### 七、常用工作流程示例
1. **日常开发流程**  
   ```bash
   git pull origin main  # 拉取最新代码  
   git checkout -b fix-bug-123  # 创建新分支  
   git add . && git commit -m "修复Bug 123"  # 提交修改  
   git push origin fix-bug-123  # 推送分支  
   # 创建Pull Request合并到主分支  # 
   ```


2. **紧急修复线上问题**  
   ```bash
   git stash  # 暂存当前工作  
   git checkout hotfix  # 切换到热修复分支  
   git add . && git commit -m "紧急修复登录问题"  
   git push origin hotfix  
   git checkout dev  # 返回原分支  
   git stash pop  # 恢复暂存修改  # 
   ```


---

### 注意事项
- **提交规范**：提交信息应清晰描述修改内容，推荐使用[Conventional Commits](https://www.conventionalcommits.org/)规范。
- **强制推送风险**：`git push --force`可能覆盖他人提交，需团队协商后使用。
- **忽略文件配置**：通过`.gitignore`文件排除临时文件（如`*.log`、`node_modules/`）。

通过掌握上述指令，开发者可高效管理代码版本、协作开发及处理复杂场景。建议结合实践逐步熟悉高级功能（如`rebase`、`bisect`等），并参考[官方文档](https://git-scm.com/doc)深化理解。