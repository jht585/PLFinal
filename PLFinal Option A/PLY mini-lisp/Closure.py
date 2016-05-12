class coffee(object):
    def outerF(self):
        menu = {
            'espresso': '$2.10',
            '*espresso': lambda x: menu.update({'espresso': x}),
            'mocha': '$4.15',
            '*mocha': lambda x: menu.update({'mocha': x}),
            'latte': '$3.65',
            '*latte': lambda x: menu.update({'latte': x}),
            'cappuccino': '$3.75',
            '*cappuccino': lambda x: menu.update({'cappuccino': x}),
            'macchiato': '$2.65',
            '*macchiato': lambda x: menu.update({'macchiato': x})
        }
        def innerF(self, item):
            if item in menu:
                return menu[item]
            else:
                return None
        return innerF
    run = outerF('whatever')

class starbucks(coffee):
    def outerF(self):
        menu = {
            'macchiato': '$4.45',
            '*macchiato': lambda x: menu.update({'macchiato': x})
        }
        def innerF(self, item):
            if item in menu:
                return menu[item]
            else:
                return super(starbucks, self).run(item)
        return innerF
    run = outerF('whatever')

'''
c1 = coffee()
s1 = starbucks()
s2 = starbucks()
print c1.run('espresso')
print s1.run('espresso')
print s2.run('espresso')
c1.run('*espresso')('$2.70')
print c1.run('espresso')
print s1.run('espresso')
print s2.run('espresso')


print c1.run('espresso')
print c1.run('mocha')
print c1.run('latte')
print c1.run('cappuccino')
print c1.run('macchiato')
c1.run('*espresso')('$2.60')
c1.run('*mocha')('$2.60')
c1.run('*latte')('$2.60')
c1.run('*cappuccino')('$2.60')
c1.run('*macchiato')('$2.60')
print
print s1.run('espresso')
print s1.run('mocha')
print s1.run('latte')
print s1.run('cappuccino')
print s1.run('macchiato')
print
s1.run('*espresso')('$3.00')
print c1.run('espresso')
print s1.run('espresso')
print
c1.run('*macchiato')('$1.00')
print c1.run('macchiato')
print s1.run('macchiato')
s1.run('*macchiato')('$5.00')
print c1.run('macchiato')
print s1.run('macchiato')
'''

