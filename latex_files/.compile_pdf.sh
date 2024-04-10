#!/bin/bash

# Define paths and filenames
source_folder="." # Assuming your LaTeX files are in the current directory
target_folder="../00_JRR-submission_folder"
main_tex_file="main.tex" # Name of your main LaTeX file
bib_file="references.bib" # Name of your bibliography file
output_pdf_name="00_T-reX_manuscript.pdf" # Desired name for the output PDF
echo "======================================================="
echo "Compiling $main_tex_file to $output_pdf_name"
# Create target folder if it doesn't exist
mkdir -p "$target_folder"
echo "======================================================="
latexmk -c $main_tex_file || exit 1
latexmk -pdf $main_tex_file || exit 1

# Clean up before compiling
# pdflatex -c "$main_tex_file" || exit 1

# # Compile LaTeX document
# pdflatex -interaction=batchmode -file-line-error "$main_tex_file"
# bibtex "${main_tex_file%.*}" # Run bibtex if needed
# pdflatex -interaction=batchmode -file-line-error "$main_tex_file"
# pdflatex -interaction=batchmode -file-line-error "$main_tex_file" # Run twice for references

# Check if PDF was generated
if [ ! -f "${main_tex_file%.*}.pdf" ]; then
    echo "PDF generation failed."
    exit 1
fi

# Move the PDF and .bib to the target folder
cp "${main_tex_file%.*}.pdf" "$target_folder/$output_pdf_name"
cp "$source_folder/$bib_file" "$target_folder/T-reX_references.bib"

# Clean up temporary files
rm -f *.aux *.log *.bbl *.blg *.idx *.ind *.lof *.lot *.out *.toc *.acn *.acr *.alg *.glg *.glo *.gls *.ist

echo "Process completed successfully."
echo "PDF saved to $target_folder/$output_pdf_name"
echo "Bibliography saved to $target_folder/T-reX_references.bib"
open "$target_folder/$output_pdf_name" # Open the PDF
echo "======================================================="
