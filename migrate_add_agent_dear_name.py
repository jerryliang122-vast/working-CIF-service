"""
数据库迁移脚本：为 agent_email_address 表添加 agent_dear_name 字段

使用方法：
1. 运行此脚本：python migrate_add_agent_dear_name.py
2. 脚本会自动为现有数据库添加 agent_dear_name 字段
3. 现有数据的 agent_dear_name 字段将默认为 "team"
"""

import sqlite3
import os


def migrate_database():
    # 数据库文件路径
    db_path = os.path.join(os.getcwd(), "conf", "agent_email.db")
    
    # 检查数据库文件是否存在
    if not os.path.exists(db_path):
        print(f"错误：数据库文件不存在：{db_path}")
        return False
    
    try:
        # 连接数据库
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # 检查字段是否已存在
        cursor.execute("PRAGMA table_info(agent_email_address)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'agent_dear_name' in columns:
            print("提示：agent_dear_name 字段已存在，无需迁移")
            conn.close()
            return True
        
        # 添加新字段
        print("正在添加 agent_dear_name 字段...")
        cursor.execute(
            "ALTER TABLE agent_email_address ADD COLUMN agent_dear_name TEXT"
        )
        
        # 为现有数据设置默认值 "team"
        print("正在为现有数据设置默认值...")
        cursor.execute(
            "UPDATE agent_email_address SET agent_dear_name = 'team' WHERE agent_dear_name IS NULL OR agent_dear_name = ''"
        )
        
        # 提交更改
        conn.commit()
        
        # 验证字段是否添加成功
        cursor.execute("PRAGMA table_info(agent_email_address)")
        columns = [column[1] for column in cursor.fetchall()]
        
        if 'agent_dear_name' in columns:
            print("✅ 迁移成功！agent_dear_name 字段已添加")
            
            # 显示数据库统计信息
            cursor.execute("SELECT COUNT(*) FROM agent_email_address")
            total_count = cursor.fetchone()[0]
            cursor.execute("SELECT COUNT(*) FROM agent_email_address WHERE agent_dear_name = 'team'")
            team_count = cursor.fetchone()[0]
            print(f"📊 数据库统计：")
            print(f"   - 总记录数：{total_count}")
            print(f"   - agent_dear_name = 'team'：{team_count}")
            
            conn.close()
            return True
        else:
            print("❌ 迁移失败：字段未添加成功")
            conn.close()
            return False
            
    except Exception as e:
        print(f"❌ 迁移过程中出现错误：{e}")
        if 'conn' in locals():
            conn.close()
        return False


if __name__ == "__main__":
    print("=" * 60)
    print("数据库迁移脚本 - 添加 agent_dear_name 字段")
    print("=" * 60)
    print()
    
    success = migrate_database()
    
    print()
    print("=" * 60)
    if success:
        print("迁移完成！现在可以重启应用程序使用新功能。")
    else:
        print("迁移失败！请检查错误信息。")
    print("=" * 60)
