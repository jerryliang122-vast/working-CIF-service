# agent_dear_name 功能迁移指南

## 📋 功能说明

在询价模块中新增了 `agent_dear_name` 字段，用于个性化邮件称呼。当发送询价邮件时，可以为每个代理设置不同的称呼（如 "Dear John" 或 "Dear team"）。

---

## 🔧 已完成的修改

### 1. 数据库模型
- **文件**: `utils/email_api/email_sql.py`
- **修改**: 在 `Agent` 类中添加了 `agent_dear_name = Column(TEXT)` 字段

### 2. 数据库操作
- **文件**: `controllers/inquiry.py`
- **新增函数**:
  - `read_dear_name(name, port)`: 读取代理的 dear_name，默认返回 "team"
- **修改函数**:
  - `write_port_name(port, name, email, agent_dear_name=None)`: 添加 `agent_dear_name` 参数支持

### 3. UI逻辑
- **文件**: `controllers/inquiry.py`
- **修改方法**:
  - `write_proxy()`: 读取UI中的 `agent_dear_name` 并保存到数据库
  - `update_addresslist()`: 选择代理时回显 `agent_dear_name` 到输入框
  - `send_email()`: 发送邮件时为每个代理获取对应的 `dear_name` 生成个性化邮件
  - `delete_data()`: 清空数据时也清空 `agent_dear_name` 输入框
  - `preview_data(dear_name="team")`: 预览时支持自定义 `dear_name`

### 4. 邮件模板
- **文件**: `utils/email_api/inquiry_smtp.py`
- **修改**: `mail_template()` 函数添加 `dear_name` 参数，将 "Dear team" 改为 "Dear {dear_name}"

---

## 🚀 迁移步骤

### 步骤1：运行数据库迁移脚本

在项目根目录下运行：

```bash
python migrate_add_agent_dear_name.py
```

此脚本会：
1. 检查 `conf/agent_email.db` 数据库文件
2. 为 `agent_email_address` 表添加 `agent_dear_name` 字段
3. 为现有数据设置默认值 "team"
4. 显示迁移结果和统计信息

**预期输出示例**:
```
============================================================
数据库迁移脚本 - 添加 agent_dear_name 字段
============================================================

正在添加 agent_dear_name 字段...
正在为现有数据设置默认值...
✅ 迁移成功！agent_dear_name 字段已添加
📊 数据库统计：
   - 总记录数：15
   - agent_dear_name = 'team'：15

============================================================
迁移完成！现在可以重启应用程序使用新功能。
============================================================
```

### 步骤2：重启应用程序

数据库迁移完成后，重启应用程序即可使用新功能。

---

## 💡 使用说明

### 1. 添加代理信息时

在添加代理信息界面，填写以下字段：
- **代理名称**: 代理的名字
- **代理邮箱**: 代理的邮箱地址（支持多个，用逗号或换行分隔）
- **Dear Name**: 邮件称呼（如 "John"、"Mary" 或 "team"）
  - 如果留空，默认保存为 "team"

### 2. 查看代理信息时

在代理列表中选择某个代理后：
- 邮箱列表会显示该代理的邮箱地址
- "Dear Name" 输入框会自动填充该代理的称呼

### 3. 发送邮件时

- 为每个选中的代理生成个性化邮件
- 邮件开头的 "Dear {dear_name}" 会使用每个代理的称呼
- 例如：
  - 代理A的 dear_name = "John" → "Dear John,"
  - 代理B的 dear_name = "team" → "Dear team,"

### 4. 预览邮件时

点击"预览"按钮，邮件模板会显示：
- 默认使用 "team"
- 发送时会使用每个代理的实际称呼

---

## 🔄 数据回滚（如需要）

如果迁移后需要回滚，可以执行以下SQL：

```sql
-- 连接到数据库
sqlite3 conf/agent_email.db

-- 删除新添加的字段
-- 注意：SQLite 不支持 DROP COLUMN，需要重建表
-- 建议先备份数据库文件
```

**更好的方法**：
1. 迁移前备份 `conf/agent_email.db`
2. 如需回滚，直接恢复备份文件

```bash
# 备份
cp conf/agent_email.db conf/agent_email.db.backup

# 恢复
cp conf/agent_email.db.backup conf/agent_email.db
```

---

## ⚠️ 注意事项

1. **数据库备份**: 建议在运行迁移脚本前备份数据库文件
2. **默认值**: 现有数据的 `agent_dear_name` 会自动设置为 "team"
3. **向后兼容**: 即使不填写 `agent_dear_name`，邮件也能正常发送（使用默认值 "team"）
4. **空值处理**: 读取时如果字段为空或NULL，会自动返回 "team"

---

## 📊 字段说明

| 字段名 | 类型 | 说明 | 默认值 |
|--------|------|------|--------|
| agent_dear_name | TEXT | 代理的邮件称呼 | "team" |

---

## 🐛 故障排查

### 问题1：迁移脚本运行失败

**解决方案**:
- 检查数据库文件路径是否正确
- 确保没有其他程序正在使用数据库文件
- 检查文件权限

### 问题2：邮件发送时没有使用个性化称呼

**解决方案**:
- 确认数据库迁移已成功完成
- 检查代理的 `agent_dear_name` 字段是否有值
- 查看应用程序日志确认是否正确读取了该字段

### 问题3：UI中输入框没有显示值

**解决方案**:
- 确认选择了代理后是否正确调用了 `update_addresslist` 方法
- 检查数据库中是否有该字段的值
- 查看应用程序日志确认查询是否成功

---

## ✅ 测试清单

迁移完成后，请测试以下功能：

- [ ] 运行迁移脚本成功
- [ ] 添加新代理时可以设置 `agent_dear_name`
- [ ] 选择代理时能正确回显 `agent_dear_name`
- [ ] 代理信息的 `agent_dear_name` 可以正常更新
- [ ] 发送邮件时使用正确的称呼
- [ ] 清空数据时 `agent_dear_name` 输入框也被清空
- [ ] 现有数据的 `agent_dear_name` 默认为 "team"

---

## 📞 技术支持

如有问题，请检查：
1. 应用程序日志
2. 数据库迁移脚本的输出
3. 数据库字段是否正确添加

---

**迁移日期**: 2026-01-26  
**版本**: 1.0
