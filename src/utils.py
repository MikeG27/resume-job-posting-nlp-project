from IPython.display import display, HTML
from bs4 import BeautifulSoup as bs

def render(html) -> None:
    """Render html files for jupyter notebook usecase"""
    display(HTML(html))
    
def read_html_from_file(path) -> bs:
    with open(path, 'r') as f:
        contents = f.read()
        soup = bs(contents, 'lxml')
        return soup
    
def show_result_with(path,only=None):
    """
    Show html files based on avaible options
    
    Only options:
        * render: print only render file
        * html: print only html
        * none: print all
    """
    html = read_html_from_file(path)
    
    if only == "render":
        render(str(html))
        
    if only == "html":
        print(html)

    else:
        render(str(html))
        print("**HTML**\n")
        print(html.prettify())
        
    return html