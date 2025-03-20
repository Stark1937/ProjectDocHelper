import inquirer
import os
from jinja2 import Environment, FileSystemLoader

def ask_questions():
    questions = [
        inquirer.List('mode',
                      message="请选择文档生成模式",
                      choices=['精简模式 (5-10 个问题)', '详细模式 (20-30 个问题)'],
                      default='精简模式 (5-10 个问题)'),
        inquirer.Text('project_name',
                      message="请输入项目名称",
                      default="My Project"),
        inquirer.Checkbox('tech_stack',
                          message="请选择技术栈 (可多选)",
                          choices=['React', 'Node.js', 'Django', 'Flask', 'Vue'],
                          default=['React'])
    ]
    answers = inquirer.prompt(questions)
    return answers

def generate_docs():
    answers = ask_questions()
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('ProjectRequirements.md.j2')
    content = template.render(
        project_name=answers['project_name'],
        tech_stack=", ".join(answers['tech_stack']),
        mode=answers['mode']
    )
    os.makedirs("docs", exist_ok=True)
    with open(os.path.join("docs", "ProjectRequirements.md"), "w") as f:
        f.write(content)
    print("文档生成成功！路径：docs/ProjectRequirements.md")