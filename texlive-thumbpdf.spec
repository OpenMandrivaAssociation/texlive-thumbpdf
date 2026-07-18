%global tl_name thumbpdf
%global tl_revision 79461
%global tl_bin_links thumbpdf:%{_texmfdistdir}/scripts/thumbpdf/thumbpdf.pl

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.17
Release:	%{tl_revision}.1
Summary:	Thumbnails for pdfTeX and dvips/ps2pdf
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/thumbpdf
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/thumbpdf.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(thumbpdf.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}
Provides:	texlive(%{tl_name}.bin) = %{tl_revision}
Provides:	texlive-%{tl_name}.bin = %{EVRD}

%description
A Perl script that provides support for thumbnails in pdfTeX and
dvips/ps2pdf. The script uses ghostscript to generate the thumbnails
which get represented in a TeX readable file that is read by the package
thumbpdf.sty to automatically include the thumbnails. This arrangement
works with both plain TeX and LaTeX.

