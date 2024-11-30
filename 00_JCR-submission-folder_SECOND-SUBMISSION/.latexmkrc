push @generated_exts, "synctex.gz";
push @generated_exts, "run.xml";
@clean_ext = qw(synctex.gz synctex.gz(busy) run.xml tex.bak bbl bcf fdb_latexmk run tdo %R-blx.bib);
# $dvi_previewer = 'start xdvi -watchfile 1.5';
# $ps_previewer  = 'start gv --watch';
# $pdf_previewer = 'start evince';
# $pdf_mode = 1;
@default_files = ('00_T-reX_manuscript.tex');
$clean_ext = "bbl nav out snm spl abs";
