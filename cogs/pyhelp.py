import discord
from discord.ext import commands

class PyHelp(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('PyHelp module loaded')

    @commands.command()
    async def syntax(self, ctx, keyword = None):
        if keyword == None:
            await ctx.send("```!py syntax [wyrażenie]\nDostępne wyrażenia:\nif\nelif\nelse```")
        elif keyword == "if":
            await ctx.send("```py\nif warunek:\n    kod```\n`if - Służy do tworzenia instrukcji warunkowych.`\nPrzykład:\n```py\nif 2>1:\n    print('prawda')\nprint('poza ifem')``` ```WAŻNE! Przy porównywaniu wartości należy użyć '==' a nie '='.```")
        elif keyword == "elif":
            await ctx.send("```py\nif warunek:\n    kod\nelif inny_warunek:\n    inny_kod```\n`elif - Jeśli poprzedni warunek okazał się fałszywy, sprawdzamy inny. Jeśli jednak byl prawdziwy, pomijamy sprawdzanie tych.`\nPrzykłady:\n```py\nif False:\n    print('Tej wiadomości nie zobaczymy')\nelif True:\n    print('Tą wiadomość zobaczymy!')```\n```py\nif True:\n    print('Tą zobaczymy')\nelif True:\n    print('A tej nie')```\n```py\nif False:\n    print('Tej nie zobaczymy')\nelif False:\n    print('Tej też nie')```")
        elif keyword == "else":
            await ctx.send("```py\nif warunek:\n    kod\nelse:\n    inny_kod```\n`else - Jeśli poprzednie warunki są fałszywe, wykonujemy ten blok`\nPrzykład:\n```py\nif False:\n    print('To się nie wykona')\nelse:\n    print('To już tak')```\n```py\nif True:\n    print('To się wykona')\nelse:\n    print('To już nie')```")
        else:
            await ctx.send("Nieznane wyrażenie. Jeśli uważasz, że powinno ono tu być, napisz do @Molipow#3955")

    @commands.command()
    async def operator(self, ctx, keyword = None):
        if keyword == None:
            await ctx.send("```!py operator [operator]\nDostępne operatory:\n+\n-\n*\n/\n%\n**\n//\n==\n!=\n>\n<\n>=\n<=\nand\nor\nnot```")
        elif keyword == "+":
            await ctx.send("`+ - operator arytmetyczny. Dodaje 2 liczby do siebie`\nPrzykład:\n```py\nprint(2+3) # wyjdzie 5```")
        elif keyword == "-":
            await ctx.send("`- - operator arytmetyczny. Odejmuje 2 liczby od siebie`\nPrzykład:\n```py\nprint(2-3) # wyjdzie -1```")
        elif keyword == "*":
            await ctx.send("`* - operator arytmetyczny. Mnoży 2 liczby przez siebie`\nPrzykład:\n```py\nprint(2*3) # wyjdzie 6```")
        elif keyword == "/":
            await ctx.send("`/ - operator arytmetyczny. Dodaje 2 liczby do siebie`\nPrzykład:\n```py\nprint(6/3) # wyjdzie 2.0\n # operator '/' zwraca wynik jako float```")
        elif keyword == "%":
            await ctx.send("`% - operator arytmetyczny. Zwraca resztę z dzielenia liczby 1 przez liczbę 2`\nPrzykład:\n```py\nprint(3%2) # wyjdzie 1```")
        elif keyword == "**":
            await ctx.send("`** - operator arytmetyczny. Zwraca liczbę 1 do potęgi liczby 2`\nPrzykład:\n```py\nprint(2**3) # wyjdzie 8```")
        elif keyword == "//":
            await ctx.send("`// - operator arytmetyczny. Zwraca całości z dzielenia liczby 1 przez liczbę 2`\nPrzykład:\n```py\nprint(3//2) # wyjdzie 1```")
        elif keyword == "==":
            await ctx.send("`== - operator porównania. Sprawdza czy argumenty są równe. Zwraca True albo False`\nPrzykład:\n```py\nprint(2==3) # wyjdzie False\nprint(3==3) # wyjdzie True```")
        elif keyword == "!=":
            await ctx.send("`!= - operator porównania. Sprawdza czy argumenty są różne. Zwraca True albo False`\nPrzykład:\n```py\nprint(2==3) # wyjdzie True\nprint(3==3) # wyjdzie False```")
        elif keyword == ">":
            await ctx.send("`> - operator porównania. Sprawdza czy argument po lewej jest większy. Zwraca True albo False`\nPrzykład:\n```py\nprint(2>3) # wyjdzie False\nprint(3>2) # wyjdzie True```")
        elif keyword == "<":
            await ctx.send("`< - operator porównania. Sprawdza czy argument po prawej jest większy. Zwraca True albo False`\nPrzykład:\n```py\nprint(2<3) # wyjdzie True\nprint(3<2) # wyjdzie False```")
        elif keyword == ">=":
            await ctx.send("`>= - operator porównania. Sprawdza czy argument po lewej jest większy lub równy. Zwraca True albo False`\nPrzykład:\n```py\nprint(2>=3) # wyjdzie False\nprint(3>=3) # wyjdzie True```")
        elif keyword == "<=":
            await ctx.send("`<= - operator porównania. Sprawdza czy argument po prawej jest większy lub równy. Zwraca True albo False`\nPrzykład:\n```py\nprint(2<=3) # wyjdzie True\nprint(3<=3) # wyjdzie True```")
        elif keyword == "and":
            await ctx.send("`and - operator logiczny. Sprawdza czy lewa i prawa strona są prawdziwe. Zwraca True albo False`\nPrzykład:\n```py\nprint(2<3 and 3==3) # wyjdzie True\nprint(2<3 and 3!=3) # wyjdzie False```")
        elif keyword == "or":
            await ctx.send("`or - operator logiczny. Sprawdza czy lewa lub prawa strona są prawdziwe. Zwraca True albo False`\nPrzykład:\n```py\nprint(2<3 or 3==3) # wyjdzie True\nprint(2<3 or 3!=3) # wyjdzie True```")
        elif keyword == "not":
            await ctx.send("`not - operator logiczny. Neguje wartość. Zwraca True albo False`\nPrzykład:\n```py\nprint(not False) # wyjdzie True\nprint(not 2<3) # wyjdzie False\nprint(not 2<3 or 3==3) # wyjdzie True\nprint(not (2<3 or 3==3)) # wyjdzie False```\n`(nawiasy mają znaczenie ;p)`")
        else:
            await ctx.send("Nieznany operator. Jeśli uważasz, że powinien on tu być, napisz do @Molipow#3955")

def setup(client):
    client.add_cog(PyHelp(client))