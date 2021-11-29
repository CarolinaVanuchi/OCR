class Latex:

    def header():
        return '\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n'
        
    def content(text):
        return '\\begin{document}\n'+text+'\n'
            
    def footer():
        return '\\end{document}'