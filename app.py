from flask import Flask, render_template, request

app = Flask(__name__, template_folder='template')

@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

@app.route('/produtos')
def produtos():
    produtos_info = [
        {'Official Light Stick Special Edition (Armybomb)': 'Produto 1', 'descricao': 'A **Official Light Stick Special Edition (Armybomb)** é a versão exclusiva e icônica do famoso bastão de luz do BTS, desenvolvido especialmente para os fãs mais dedicados do grupo, os ARMYs. Com um design sofisticado e detalhes únicos, essa edição especial traz elementos exclusivos que representam a conexão entre os fãs e o grupo, além de funcionalidades aprimoradas, como diferentes modos de iluminação e a capacidade de sincronizar com performances ao vivo. O Armybomb é perfeito para quem quer ter uma experiência mais imersiva e marcante nos shows ou para exibir com orgulho como parte da sua coleção de fã. Elegante e cheia de significado, essa edição limitada é um verdadeiro item de desejo para qualquer ARMY.', 'preco': 'R$ 590,00', "imagem": "bts.1.webp"}
        ,{'Copo Térmico Bts Personagens Grupo Coreano K-pop - Banda': 'Produto 2', 'descricao': 'O **Copo Térmico BTS Personagens - Grupo Coreano K-pop** é o acessório perfeito para os fãs de BTS que querem manter suas bebidas na temperatura ideal enquanto demonstram todo o amor pela banda! Com um design exclusivo, o copo apresenta personagens carismáticos dos membros do BTS, trazendo um toque único e vibrante à sua rotina. Ideal para o dia a dia, seja no trabalho, escola ou na hora do lazer, o copo térmico mantém suas bebidas quentes ou geladas por mais tempo, combinando funcionalidade e estilo. Feito com materiais de alta qualidade, ele é resistente, durável e fácil de transportar, sendo a escolha ideal para quem quer carregar a energia do BTS em qualquer lugar!', 'preco': 'R$ 48,00', "imagem": "bts,2.webp"}
        ]

    return render_template('produtos.html', produtos=produtos_info)

@app.route('/sobre')
def sobre():
    membros = [
        {'kim taehyung': 'Membro 1', 'foto': 'membro1.webp', 'descricao': 'Kim Tae-hyung, mais conhecido profissionalmente como V, é um cantor, dançarino, compositor, produtor musical e ator sul-coreano.'},
        {'Jeon Jung-kook': 'Membro 2', 'foto': 'membro2.webp', 'descricao': 'Jeon Jung-kook OMC, mais frequentemente creditado na carreira musical apenas como Jungkook, é um cantor, compositor, dançarino e produtor musical sul-coreano. Jungkook ganhou destaque mundial como membro do grupo masculino BTS, formado em 2013.'}
    ]
    return render_template('sobre.html', membros=membros)

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port=5000)