# Contributing to Baize
感谢你有兴趣为 Baize 做贡献！我们欢迎各种形式的参与，包括报告问题、提交代码、改进文档、提出建议等。

# 目录
- 行为准则
- 如何贡献
报告问题

提交代码

开发流程
- 代码风格与测试
- 提交信息规范
- 许可证与贡献者许可协议（CLA）
- 当前许可证
- 为什么需要 CLA
- 个人贡献者
- 公司贡献者
- 如何签署
- 已合并贡献的重新许可
- 联系方式

# 行为准则
参与本项目即表示你同意遵守我们的 行为准则。请保持友善、尊重和包容。

# 如何贡献
## 报告问题
- 使用 GitHub Issues 报告 bug 或提出功能建议。
- 搜索现有 issue，避免重复。
- 提供清晰的标题、复现步骤、预期行为和实际行为。
- 如果可能，附上环境信息和截图。

## 提交代码
1.Fork 本仓库。

2.创建你的特性分支：git checkout -b feature/your-feature-name。

3.提交你的更改：git commit -m "feat: add some feature"。

4.推送到分支：git push origin feature/your-feature-name。

5.在 GitHub 上打开 Pull Request。

在提交 PR 之前，请确保：
- 代码通过现有测试。
- 更新了相关文档。
- 遵守代码风格。
- 你已经阅读并同意本文件中的许可证条款。

## 开发流程
```bash
# 克隆仓库
git clone https://github.com/Xu123-Bob/Baize.git
cd Baize

# 安装依赖
pip install -r requirements.txt
pip install -r requirements-data.txt

```
## 代码风格与测试
- 遵循项目现有的代码风格。
- 新增功能请添加相应的测试。
- 确保所有测试通过后再提交 PR。
- 如果项目有 lint 工具，请在提交前运行。

## 提交信息规范
我们使用 Conventional Commits 规范：

```text
<类型>[可选作用域]: <描述>

[可选正文]

[可选脚注]
```
常用类型：`feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`。

# 许可证与贡献者许可协议（CLA）
## 当前许可证
本项目当前使用**MIT License**。我们保留在未来采用其他开源许可证（包括但不限于 Apache License 2.0）的权利，以便更好地适应项目发展和社区需求。

旧版本将以 MIT 许可证永久发布。任何许可证变更仅适用于未来的新版本。

## 为什么需要 CLA
为了保持项目许可证的灵活性，并确保所有贡献都具备清晰的法律依据，我们要求贡献者签署**贡献者许可协议（CLA）**。

签署 CLA **不会**让你失去对自己贡献的版权。你仍然保留版权，只是授予项目维护者一项永久、全球、免版税、不可撤销的许可，允许我们将你的贡献按当前或未来的许可证进行分发和重新许可。

## 个人贡献者
如果你以**个人身份**贡献，请签署**个人贡献者许可协议（ICLA）**。你可以通过以下方式签署：

- 直接回复 PR 中的 CLA 机器人提示。

如果你在 PR 中手动确认，请回复以下声明：
```
I agree to the terms of the Individual Contributor License Agreement (ICLA) and license my contributions under the project's current and future licenses.
```
中文意思：
```
我同意个人贡献者许可协议（ICLA）的条款，并授权我的贡献按项目当前及未来的许可证发布。
```
## 公司贡献者
如果你代表**公司**或**雇主**贡献，且你的贡献可能归公司所有，则需要由公司授权代表签署**公司贡献者许可协议（CCLA）**。

CCLA 必须由有权代表公司签署法律合同的人（如法务、高管或 OSS 合规负责人）签署，提交 PR 的工程师本人通常无权签署。

签署 CCLA 后，公司需指定一名**CLA Manage**r，并将你（贡献者）的 GitHub 账号或邮箱加入授权贡献者名单。之后你的贡献将被自动识别为受 CCLA 覆盖。

**CCLA 模板与签署方式：**

- 我们采用 **Apache 基金会 CCLA 模板**。

- 签署方式：

1.电子签名：通过 [DocuSign / EasyCLA / 其他工具] 在线签署。

2.邮件签署：下载 CCLA PDF，打印签字后扫描发送至 [826741152@qq.com]。

3.PGP 签名：填写 PDF 后使用 PGP 分离签名，发送文件与签名至 [826741152@qq.com]。

4.如果你不确定是否需要公司签署，请先联系 [826741152@qq.com] 说明情况。

公司授权代表确认语句：
```
On behalf of [Company], we confirm that [Company] owns or has sufficient rights to the contributions submitted by [Name] in [PR/commit IDs], and has authority to grant this permission. We agree to license those contributions under the project's current and future licenses.
```
中文意思：
```
代表 [Company]，我们确认 [Company] 拥有或拥有足够权利处理 [Name] 在 [PR/commit IDs] 中提交的贡献，并有权授予此许可。我们同意将这些贡献按项目当前及未来的许可证发布。
```
## 如何签署
- 在提交 PR 时，CLA 机器人会自动检查你是否已签署。
- 如果未签署，机器人会提供链接和指引。
- 个人贡献者按 ICLA 流程签署。
- 公司贡献者请联系你的公司法务/OSS 合规团队，按 CCLA 流程签署，并将你加入授权名单。
- 签署完成后，重新触发 PR 检查即可。

如果你对 CLA 流程有任何疑问，请发邮件至 [826741152@qq.com] 或在本仓库开 Issue 询问。

## 已合并贡献的重新许可
对于在本项目采用 CLA 之前已经合并的贡献，如果未来我们需要变更许可证，会单独联系贡献者或其所属公司，获得明确同意后再进行重新许可。

我们尊重每一位贡献者的决定。如果无法获得重新许可同意，我们将保留 MIT 许可证，或重写相关代码。

## 联系方式
项目维护者：[徐鑫 / GitHub ID]

邮箱：[826741152@qq.com]

Issue 跟踪：[[GitHub Issues 链接](https://github.com/Xu123-Bob/Baize/issues)]

再次感谢你的贡献！