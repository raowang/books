#!/usr/bin/env python3
"""Convert Markdown files to LaTeX chapters."""

import re
import os

def md_to_latex(md_content):
    """Convert markdown content to LaTeX."""
    lines = md_content.split('\n')
    result = []
    in_list = False
    in_code_block = False

    for line in lines:
        # Code blocks
        if line.strip().startswith('```'):
            if in_code_block:
                result.append('\\end{lstlisting}')
                in_code_block = False
            else:
                result.append('\\begin{lstlisting}')
                in_code_block = True
            continue

        if in_code_block:
            result.append(line)
            continue

        # Headers
        if line.startswith('# '):
            text = line[2:].strip()
            result.append(f'\\chapter{{{text}}}\n')
        elif line.startswith('## '):
            text = line[3:].strip()
            result.append(f'\\section{{{text}}}\n')
        elif line.startswith('### '):
            text = line[4:].strip()
            result.append(f'\\subsection{{{text}}}\n')
        elif line.startswith('#### '):
            text = line[5:].strip()
            result.append(f'\\subsubsection{{{text}}}\n')
        # Horizontal rule
        elif line.strip() == '---':
            result.append('\\hline\\newpage')
        # Empty line
        elif line.strip() == '':
            result.append('')
        # List items
        elif line.strip().startswith('- '):
            if not in_list:
                result.append('\\begin{itemize}')
                in_list = True
            text = line.strip()[2:]
            # Handle **bold** inside
            text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
            result.append(f'\\item {text}')
        elif line.strip().startswith('* '):
            if not in_list:
                result.append('\\begin{itemize}')
                in_list = True
            text = line.strip()[2:]
            text = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', text)
            result.append(f'\\item {text}')
        # Close list on non-list
        elif in_list:
            result.append('\\end{itemize}')
            in_list = False

        # Bold and italic
        line = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', line)
        line = re.sub(r'\*(.+?)\*', r'\\textit{\1}', line)

        # Blockquotes (skip for now)
        if line.strip().startswith('>'):
            continue

        # Regular text
        if line.strip() and not in_list:
            result.append(line)

    if in_list:
        result.append('\\end{itemize}')

    return '\n'.join(result)

def convert_file(input_path, output_path):
    """Convert a single markdown file to LaTeX."""
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    latex_content = md_to_latex(content)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(latex_content)

    print(f"Converted: {input_path} -> {output_path}")

# File mappings
files = [
    ('前言.md', 'latex/preface.tex'),
    ('PART-I-时代背景.md', 'latex/part-i.tex'),
    ('第一章-AI不是风口是文明级转折.md', 'latex/chapter01.tex'),
    ('第二章-德鲁克为什么还没过时.md', 'latex/chapter02.tex'),
    ('第三章-旧逻辑失灵的五个信号.md', 'latex/chapter03.tex'),
    ('PART-II-思维重构.md', 'latex/part-ii.tex'),
    ('第四章-从预测到塑造.md', 'latex/chapter04.tex'),
    ('第五章-效率思维的陷阱.md', 'latex/chapter05.tex'),
    ('第六章-最佳实践的半衰期.md', 'latex/chapter06.tex'),
    ('第七章-韧性优先.md', 'latex/chapter07.tex'),
    ('PART-III-流程重构.md', 'latex/part-iii.tex'),
    ('第八章-控制逻辑的失效.md', 'latex/chapter08.tex'),
    ('第九章-质量管理的新逻辑.md', 'latex/chapter09.tex'),
    ('第十章-决策的人机分工.md', 'latex/chapter10.tex'),
    ('第十一章-创新需要制度化.md', 'latex/chapter11.tex'),
    ('PART-IV-组织重构.md', 'latex/part-iv.tex'),
    ('第十二章-组织架构的哲学.md', 'latex/chapter12.tex'),
    ('第十三章-中间层之死.md', 'latex/chapter13.tex'),
    ('第十四章-跨边界协作.md', 'latex/chapter14.tex'),
    ('第十五章-授权下沉一线.md', 'latex/chapter15.tex'),
    ('第十六章-韧性优先.md', 'latex/chapter16.tex'),
    ('PART-V-技能重构.md', 'latex/part-v.tex'),
    ('第十七章-技能经济学的重构.md', 'latex/chapter17.tex'),
    ('第十八章-T型能力的进化.md', 'latex/chapter18.tex'),
    ('第十九章-判断力.md', 'latex/chapter19.tex'),
    ('第二十章-人机协作技能.md', 'latex/chapter20.tex'),
    ('第二十一章-关系技能.md', 'latex/chapter21.tex'),
    ('PART-VI-阻力维度.md', 'latex/part-vi.tex'),
    ('第二十二章-最强大的变革阻力来自群体.md', 'latex/chapter22.tex'),
    ('第二十三章-三类既得利益者的转型困境.md', 'latex/chapter23.tex'),
    ('第二十四章-变革联盟与软着陆路径.md', 'latex/chapter24.tex'),
    ('PART-VII-面向未来.md', 'latex/part-vii.tex'),
    ('第二十五章-如果德鲁克今天写动荡时代的管理.md', 'latex/chapter25.tex'),
    ('第二十六章-管理者的下一步.md', 'latex/chapter26.tex'),
    ('第二十七章-结语.md', 'latex/chapter27.tex'),
]

base_dir = '/Users/uu/workspaces/books/Beyond-Control'
for md_file, tex_file in files:
    input_path = os.path.join(base_dir, md_file)
    output_path = os.path.join(base_dir, tex_file)
    if os.path.exists(input_path):
        convert_file(input_path, output_path)
    else:
        print(f"Skipped (not found): {input_path}")

print("Done!")
