from exp1_lrinterp_gram import parser

def exp1_lrinterp(input_stream = None):
    'A driver for our LR Exp1 interpreter.'
    
    if not input_stream:
        input_stream = input("exp1 > ")
    
    parser.parse(input_stream)
