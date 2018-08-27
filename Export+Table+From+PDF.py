#import tabula_py not tabula
from tabula import read_pdf

path_to_pdf = r"<Path>\data\Sample_employees_data.pdf"
df = read_pdf(path_to_pdf ,pages=1,guess=False)

df




