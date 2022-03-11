glossary={
    'python':'programming language',
    'tuple':'immutable list',
    'list' :'collection of items in a particular order' ,
    'loop' : 'looping allows you to do same action, or set of actions,with every item in list'}

for language, meanings in glossary.items():
    
    print(f'{language.title()} :{meanings.title()}')