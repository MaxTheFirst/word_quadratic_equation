from win32com import __gen_path__
import win32com.client as win32
from calc import get_decision
from os import walk
from shutil import rmtree


def get_selections():
    try:
        word = win32.gencache.EnsureDispatch('Word.Application')
        word.ActiveDocument
    except AttributeError:
        paths = list(walk(__gen_path__))
        rmtree(paths[0][0] + '\\' + paths[0][1][0])
        return get_selections()
    return word.Selection


def main():
    doc, selection = get_selections()
    omaths = selection.OMaths(1)
    omaths.Linearize()
    result_strings = get_decision(selection.Range.Text.strip())
    omaths.BuildUp()
    selection.Collapse(0)
    for i in reversed(result_strings):
        selection = doc.Content.Paragraphs.Add(selection.Range)
        selection.Range.InsertParagraphAfter()
        selection.Range.Text = i
        math = doc.OMaths.Add(selection.Range).OMaths(1)
        math.BuildUp() 
        math.Type = win32.constants.wdOMathInline
        
        
if __name__ == '__main__':
    main()
    
    
