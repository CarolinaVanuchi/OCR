class Latex:

    def header():
        return '\\documentclass{article}\n\\usepackage{graphicx}\n'
        
    def content(text):
        return '\\begin{document}\n'+text
            
    def footer():
        return '\\end{document}'

    def add_image(caption, path, author, figure_name):
        return '\\begin{figure}[!h] \n\\centering \n\\caption{'+caption+'} \n\\includegraphics[height=6cm]{'+path+'} \n Fonte: '+author+'\n \\end{figure}\n'