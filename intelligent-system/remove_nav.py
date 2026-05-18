import re

content = open('d:/git_development/prototype/intelligent-system/index_v7.html', encoding='utf-8').read()

to_remove = ['nav-profiler', 'nav-multiWallet', 'nav-backtest', 'nav-rebalancer', 'nav-stratCompare', 'nav-alertsHistory', 'nav-aiAdvisor']

for nav_id in to_remove:
    pattern = r'\s*<div class="nav-item[^"]*" id="' + nav_id + r'"[^>]*>.*?</div>'
    new_content = re.sub(pattern, '', content, flags=re.DOTALL)
    if new_content == content:
        print(f'WARNING: {nav_id} not found')
    else:
        content = new_content
        print(f'Removed {nav_id}')

open('d:/git_development/prototype/intelligent-system/index_v7.html', 'w', encoding='utf-8').write(content)
print('Done. Lines:', content.count('\n'))
