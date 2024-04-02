$pdflatex = 'pdflatex -interaction=batchmode -file-line-error %O %S';
# $clean_ext = 'aux bbl blg idx ind lof lot out toc acn acr alg glg glo gls ist';

# # Define target folder
# my $target_folder = "../00_JRR-submission_folder";

# # Clean up before compiling
# system("latexmk -c");

# add_cus_dep('pdf', 'done', 0, 'move_files');

# sub move_files {
#     # Check if target folder exists, if not create it
#     unless(-d $target_folder) {
#         mkdir $target_folder or die "Could not create $target_folder: $!";
#     }

#     # Clean up after compiling
#     system("latexmk -c");

#     # Move the PDF and references.bib to the correct folder
#     system("cp main.pdf $target_folder/00_T-reX_manuscript.pdf");
#     system("cp references.bib $target_folder/T-reX_references.bib");
# }
