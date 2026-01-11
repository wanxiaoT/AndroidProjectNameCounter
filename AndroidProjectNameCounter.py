import os
from pathlib import Path
from collections import defaultdict

def count_code_stats(project_path):
    """统计 Android Studio 项目的代码"""
    
    # 要统计的文件扩展名
    code_extensions = {
        '.kt': 'Kotlin',
        '.java': 'Java',
        '.xml': 'XML',
        '.gradle': 'Gradle',
        '.kts': 'Gradle KTS',
        '.json': 'JSON',
        '.properties': 'Properties',
    }
    
    # 要排除的目录
    exclude_dirs = {
        'build', '.gradle', '.idea', 'gradle', 
        '__pycache__', 'node_modules', '.git'
    }
    
    # 统计数据
    stats = defaultdict(lambda: {'files': 0, 'lines': 0, 'chars': 0, 'chars_no_space': 0})
    total_files = 0
    total_lines = 0
    total_chars = 0
    total_chars_no_space = 0
    
    project_path = Path(project_path)
    
    if not project_path.exists():
        print(f"❌ 错误：路径不存在 - {project_path}")
        return
    
    print(f"\n🔍 正在扫描项目: {project_path}\n")
    print("=" * 60)
    
    # 遍历项目目录
    for root, dirs, files in os.walk(project_path):
        # 排除不需要的目录
        dirs[:] = [d for d in dirs if d not in exclude_dirs]
        
        for file in files:
            file_path = Path(root) / file
            ext = file_path.suffix.lower()
            
            # 检查是否是代码文件
            if ext in code_extensions:
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read()
                        lines = content.count('\n') + 1
                        chars = len(content)
                        chars_no_space = len(content.replace(' ', '').replace('\n', '').replace('\t', '').replace('\r', ''))
                        
                        file_type = code_extensions[ext]
                        stats[file_type]['files'] += 1
                        stats[file_type]['lines'] += lines
                        stats[file_type]['chars'] += chars
                        stats[file_type]['chars_no_space'] += chars_no_space
                        
                        total_files += 1
                        total_lines += lines
                        total_chars += chars
                        total_chars_no_space += chars_no_space
                        
                except Exception as e:
                    print(f"⚠️ 无法读取文件: {file_path}")
    
    # 输出统计结果
    print(f"{'文件类型':<15} {'文件数':<10} {'行数':<12} {'字符数':<15} {'字符(无空格)':<15}")
    print("-" * 60)
    
    for file_type, data in sorted(stats.items(), key=lambda x: x[1]['chars_no_space'], reverse=True):
        print(f"{file_type:<15} {data['files']:<10} {data['lines']:<12,} {data['chars']:<15,} {data['chars_no_space']:<15,}")
    
    print("=" * 60)
    print(f"{'📊 总计':<15} {total_files:<10} {total_lines:<12,} {total_chars:<15,} {total_chars_no_space:<15,}")
    print("=" * 60)
    
    # 额外统计信息
    print(f"\n📈 详细统计:")
    print(f"   • 总文件数: {total_files:,} 个")
    print(f"   • 总代码行数: {total_lines:,} 行")
    print(f"   • 总字符数: {total_chars:,} 字符")
    print(f"   • 总字符数(不含空格): {total_chars_no_space:,} 字符")
    
    # 估算中文字数（假设平均每个中文字符占3字节）
    print(f"\n💡 提示: 如果代码主要是英文，约等于 {total_chars_no_space:,} 个字符")
    
    return {
        'total_files': total_files,
        'total_lines': total_lines,
        'total_chars': total_chars,
        'total_chars_no_space': total_chars_no_space,
        'by_type': dict(stats)
    }


def main():
    print("    Android Studio 项目代码量统计工具")
    print("    By wanxiaoT")
    print("    Github: https://github.com/wanxiaoT")
    
    # 获取用户输入
    project_path = input("\n📁 请输入 Android Studio 项目路径: ").strip()
    
    # 去除可能的引号
    project_path = project_path.strip('"').strip("'")
    
    if not project_path:
        print("❌ 错误：请输入有效的路径")
        return
    
    # 执行统计
    result = count_code_stats(project_path)
    
    if result:
        print("\n✅ 统计完成！")
    
    input("\n按 Enter 键退出...")


if __name__ == "__main__":
    main()
