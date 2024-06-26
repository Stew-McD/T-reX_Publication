#!/bin/bash

# Define paths and filenames
source_folder="."
 # Assuming your LaTeX files are in the current directory
target_folder="../00_JRR-submission_folder"
main_tex_file="main.tex"                   
bib_file="references.bib"                  
output_pdf_name="00_T-reX_manuscript.pdf"  
output_docx_name="00_T-reX_manuscript.docx"
output_html_name="00_T-reX_manuscript.html"

# Optional: Specify Pandoc templates for DOCX and HTML
docx_template="path/to/docx_template.docx"
html_template="path/to/html_template.html"

echo "======================================================="
echo "Compiling $main_tex_file to PDF, DOCX, and HTML"

# Create target folder if it doesn't exist
mkdir -p "$target_folder"

# Clean up before compiling
latexmk -c -outdir="$target_folder" "$source_folder/$main_tex_file" || exit 1

# Compile LaTeX document to PDF, output directly to target folder
latexmk -pdf -outdir="$target_folder" "$source_folder/$main_tex_file" || exit 1

# Conversion commands for DOCX and HTML with template usage if available
if [ -f "$docx_template" ]; then
    pandoc -s "$target_folder/${main_tex_file%.*}.pdf" --reference-doc="$docx_template" -o "$target_folder/$output_docx_name" || exit 1
else
    pandoc -s "$target_folder/${main_tex_file%.*}.pdf" -o "$target_folder/$output_docx_name" || exit 1
fi

if [ -f "$html_template" ]; then
    pandoc -s "$target_folder/${main_tex_file%.*}.pdf" --template="$html_template" -o "$target_folder/$output_html_name" || exit 1
else
    pandoc -s "$target_folder/${main_tex_file%.*}.pdf" -o "$target_folder/$output_html_name" || exit 1
fi

echo "Process completed successfully."
echo "PDF saved to $target_folder/$output_pdf_name"
echo "DOCX saved to $target_folder/$output_docx_name"
echo "HTML saved to $target_folder/$output_html_name"
echo "======================================================="



##OLDVERSION

# #!/bin/bash
# 
# # Define paths and filenames
# source_folder="." # Assuming your LaTeX files are in the current directory
# target_folder="../00_JRR-submission_folder"
# main_tex_file="main.tex"                    # Name of your main LaTeX file
# bib_file="references.bib"                   # Name of your bibliography file
# output_pdf_name="00_T-reX_manuscript.pdf"   # Desired name for the output PDF
# output_docx_name="00_T-reX_manuscript.docx" # Desired name for the output DOCX
# output_html_name="00_T-reX_manuscript.html" # Desired name for the output HTML
# 
# echo "======================================================="
# echo "Compiling $main_tex_file to $output_pdf_name, $output_docx_name, and $output_html_name"
# 
# # Create target folder if it doesn't exist
# mkdir -p "$target_folder"
# 
# # Clean up before compiling
# latexmk -c $main_tex_file || exit 1
# 
# # Compile LaTeX document to PDF
# latexmk -pdf $main_tex_file || exit 1
# 
# # Check if PDF was generated
# if [ ! -f "${main_tex_file%.*}.pdf" ]; then
	# echo "PDF generation failed."
	# exit 1
# fi
# 
# # Convert PDF to DOCX
# pandoc -s "${main_tex_file%.*}.pdf" -o "$target_folder/$output_docx_name" || exit 1
# 
# # Convert PDF to HTML
# pandoc -s "${main_tex_file%.*}.pdf" -o "$target_folder/$output_html_name" || exit 1
# 
# # Move the PDF and .bib to the target folder
# cp "${main_tex_file%.*}.pdf" "$target_folder/$output_pdf_name"
# cp "$source_folder/$bib_file" "$target_folder/T-reX_references.bib"
# 
# # Clean up temporary files
# rm -f *.aux *.log *.bbl *.blg *.idx *.ind *.lof *.lot *.out *.toc *.acn *.acr *.alg *.glg *.glo *.gls *.ist *.spl *.fls *.fdb_latexmk *.synctex.gz *.bcf *.run.xml
# 
# echo "Process completed successfully."
# echo "PDF saved to $target_folder/$output_pdf_name"
# echo "DOCX saved to $target_folder/$output_docx_name"
# echo "HTML saved to $target_folder/$output_html_name"
# open "$target_folder/$output_pdf_name" # Open the PDF
# echo "======================================================="
