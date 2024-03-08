#!/bin/bash
echo "================================================================================"
echo "Compiling the T-reX manuscript..."
echo "-------------------------------------------------------------------------------"
# Clean the project
echo "Cleaning the project..."
echo "-------------------------------------------------------------------------------"
latexmk -C
echo "-------------------------------------------------------------------------------"
# Compile the project
echo "Compiling the project..."
echo "-------------------------------------------------------------------------------"
latexmk -pdf -quiet main.tex
echo
echo "-------------------------------------------------------------------------------"
echo "Done compiling the T-reX manuscript."
echo "-------------------------------------------------------------------------------"
# Copy the output PDF to the specified directory
cp main.pdf ../reviews/T-reX_Manuscript_V2/T-reX_manuscript_V2.pdf

echo "Copied the output PDF to ../reviews/T-reX_Manuscript_V2/T-reX_manuscript_V2.pdf"
echo "Opening the PDF..."
echo "================================================================================"
echo " ----------------------           FIN!               ---------------------------"           
echo "================================================================================"
echo 
echo
# Open the PDF with the default viewer in a detached process
# nohup xdg-open ../reviews/T-reX_Manuscript_V2/T-reX_manuscript_V2.pdf > /dev/null 2>&1 &
