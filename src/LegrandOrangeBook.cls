\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{LegrandOrangeBook}[2022/01/26 The Legrand Orange Book Class v3.0]
% \DeclareOption*{\PassOptionsToClass{\CurrentOption}{extbook}} % Pass through any options to the base class
% \ProcessOptions\relax % Process given options
\LoadClass[9pt, twoside]{extbook} % Load the base class
\usepackage{graphicx} % Required for including pictures
\graphicspath{{Images/}} % Specifies the directory where pictures are stored
\usepackage{float} % Allows more precisely positioning floats e.g. \begin{figure}[H]
\usepackage[usenames, svgnames, table]{xcolor} % Required for defining and using custom colors
\usepackage{calc} % For simpler calculations - used for spacing the index letter headings correctly
\usepackage{changepage} % Required for temporarily indenting text blocks
\usepackage[toc]{appendix} % Required for the appendices chapters
\usepackage{etoolbox} % Required for conditional logic and easily changing commands

%----------------------------------------------------------------------------------------
%	MARGINS
%----------------------------------------------------------------------------------------


% popular page size in Amazon's KDP
% \RequirePackage[
%     paperwidth=6.14in,
%     paperheight=9.21in,
%     left=0.82in,
%     right=0.695in,
%     top=0.6in,
%     bottom=0.71in,
%     twoside,
%     headsep=0.15in,
%     includehead,
%     includefoot
% ]{geometry}





%----------------------------------------------------------------------------------------
%	MARGINS
%----------------------------------------------------------------------------------------

% 	inner=3cm, % Inner margin (left on odd pages, right on even or left in oneside mode)
	% outer=3cm, % Outer margin (right on odd pages, left on even or right in oneside mode)
	
	% headheight=0.5cm, % Header height
	% footskip=1.4cm, % Space from the bottom margin to the baseline of the footer
	
	%showframe, % Uncomment to show how the type block is set on the page


	% popular page size in Amazon's KDP
	\RequirePackage[
		paperwidth=6.00in,
		paperheight=9.00in,
		left=0.75in,
		right=0.625in,
	%     left=0.82in,
	%     right=0.695in,
		top=1.0in,
		bottom=0.71in,
	twoside,
	%     headsep=0.15in,
	%     includehead,
	 %    includefoot
		%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% pokazuje ramki na stronach: showframe
	]{geometry}
	
	
	


%----------------------------------------------------------------------------------------
%	FONTS
%----------------------------------------------------------------------------------------

\usepackage[utf8]{inputenc} % Required for inputting international characters
\usepackage[T1]{fontenc} % Output font encoding for international characters

\usepackage[final]{microtype} % Improve typography

\usepackage{fancyhdr} % Required for customizing headers and footers
\pagestyle{fancy} % Enable the custom headers and footers

\renewcommand{\headrulewidth}{0.5pt} % Top horizontal rule thickness

\renewcommand{\chaptermark}[1]{\markboth{\sffamily\normalsize\bfseries\chaptername\ \thechapter.~#1}{}} % Redefine the styling of the current chapter name in the header
\renewcommand{\sectionmark}[1]{\markright{\sffamily\normalsize\thesection~#1}{}} % Redefine the styling of the current section name in the header

\fancyhf{} % Clear default headers and footers

\fancyhead[LE, RO]{\sffamily\thepage} % Header for left even pages and right odd pages

\fancyhead[LO]{\rightmark} % Header for left odd pages

\fancyhead[RE]{\leftmark} % Header for right even pages

\fancypagestyle{plain}{ % Style for when a plain pagestyle is specified
	\fancyhead{} % Clear headers
	\renewcommand{\headrulewidth}{0pt} % Remove header rule
}

\usepackage{emptypage} % This package removes headers and footers on empty pages between chapters

%----------------------------------------------------------------------------------------
%	SECTION STYLING
%----------------------------------------------------------------------------------------

% \setcounter{secnumdepth}{3} % Number sections down to subsubsections, a value of 2 will number to subsections only and 1 to sections only

\usepackage[
	explicit, % Specify section names explicitly in \titleformat with #1
	newparttoc, % Required for writing the part toc entry number in a standard way (overriding default LaTeX behavior) so the titletoc package can style it
]{titlesec} % Required for modifying sections

%-------------------------------------------

% Command to create and output the parts pages
\newcommand{\outputpartpage}[2]{
	\begin{tikzpicture}[remember picture, overlay]
		\node[anchor=center, rectangle, fill=ocre!20, inner sep=0pt, minimum height=\paperheight, minimum width=\paperwidth] at (current page.center) {}; % Background color
		\node[anchor=north west, inner sep=0pt, xshift=\Gm@lmargin, yshift=-\Gm@tmargin] at (current page.north west) {\fontsize{220pt}{220pt}\selectfont\sffamily\bfseries\textcolor{ocre!40}{#1}}; % Part number
		\node[anchor=north east, inner sep=0pt, xshift=-\Gm@rmargin, yshift=-\Gm@tmargin] at (current page.north east) {\fontsize{30pt}{30pt}\selectfont\sffamily\bfseries\textcolor{white}{\strut #2}}; % Part title
		\node[anchor=south east, inner sep=0pt, xshift=-\Gm@rmargin, yshift=\Gm@bmargin] at (current page.south east) { % Mini table of contents
			\parbox[t][][t]{8.5cm}{ % Width of box holding the mini ToC
				\printcontents[part]{l}{0}{\setcounter{tocdepth}{1}} % Display the mini table of contents showing chapters and sections, change tocdepth to 2 to also show subsections or 0 to only show chapters
			}
		};
	\end{tikzpicture}
}

\titleformat
	{\part} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\startcontents[part]\outputpartpage{\thepart}{#1}} % Format of the whole section
	{} % Format of the section label
	{0em} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

%-------------------------------------------

% Command to store the current chapter image to use for all future chapters, can be changed any time in the document and can be empty
\newcommand{\thechapterimage}{}
\newcommand{\chapterimage}[1]{\renewcommand{\thechapterimage}{#1}}

% Command to store the current whitespace above the chapter title box for all future chapters, can be changed at any time in the document
\newcommand{\thechapterspaceabove}{}
\newcommand{\chapterspaceabove}[1]{\renewcommand{\thechapterspaceabove}{#1}}

% Command to store the current whitespace below the chapter title box for all future chapters, can be changed at any time in the document
\newcommand{\thechapterspacebelow}{}
\newcommand{\chapterspacebelow}[1]{\renewcommand{\thechapterspacebelow}{#1}}

% Command to output the chapter title with optional background image
\newcommand{\outputchaptertitle}[2]{
	\begin{tikzpicture}[remember picture,overlay]
		% If a chapter image has been specified
		\expandafter\ifstrequal\expandafter{\thechapterimage}{}{}{
			% Output the chapter image
			\node[
				anchor=north west, % Anchor point on the image
				inner sep=0pt, % Inner padding
			] at (current page.north west) {\includegraphics[width=\paperwidth]{\thechapterimage}};
		}
		% Box with the chapter title
		\draw[anchor=west] (current page.north west) node [
			anchor=north west, % Anchor point of the chapter box
			xshift=\Gm@lmargin, % Horizontal distance from the left side of the page
			yshift=-\thechapterspaceabove, % Vertical distance from the top of the page
			line width=2pt, % Border line thickness
			rounded corners=10pt, % Rounded corners amount
			draw=ocre, % Border line color
			fill=black!5, % Box background color
			fill opacity=0.6, % Background transparency
			text opacity=1, % Text transparency
			inner ysep=12.5pt, % Inner vertical padding
			inner xsep=20pt, % Inner horizontal padding
			align=flush left, % Text alignment inside box
			text width=1.2\linewidth, % Box width (wider than page to go off the right side)
			font=\huge\sffamily\bfseries, % Font styling for chapter title
		] {\parbox{0.85\linewidth}{\strut\raggedright\expandafter\ifstrequal\expandafter{#1}{}{}{#1. }#2\vspace{-3pt}}}; % Chapter title in a fixed width box for wrapping
	\end{tikzpicture}
}

% Numbered chapters
\titleformat
	{\chapter} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\outputchaptertitle{\thechapter}{#1}} % Format of the whole section
	{} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

% Unnumbered chapters
\titleformat
	{name=\chapter, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\outputchaptertitle{}{#1}} % Format of the whole section
	{} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\chapter}{0pt}{0pt}{\thechapterspacebelow} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\section} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\Large} % Format of the whole section
	{\llap{\textcolor{ocre}{\thesection}\hspace{1em}}#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label
	
\titleformat
	{name=\section, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\Large} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\section}{0pt}{12pt}{6pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\subsection} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\large} % Format of the whole section
	{\llap{\textcolor{ocre}{\thesubsection}\hspace{1em}}#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label
	
\titleformat
	{name=\subsection, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily\large} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\subsection}{0pt}{12pt}{4pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\subsubsection} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{\llap{{\thesubsubsection}\hspace{1em}}#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label
	
\titleformat
	{name=\subsubsection, numberless} % Section type being modified
	[block] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{#1} % Format of the section label
	{0cm} % Space between the title and label
	{} % Code before the label
	[] % Code after the label

\titlespacing*{\subsubsection}{0pt}{8pt}{4pt} % Spacing around section titles, the order is: left, before and after

%-------------------------------------------

\titleformat
	{\paragraph} % Section type being modified
	[runin] % Shape type, can be: hang, block, display, runin, leftmargin, rightmargin, drop, wrap, frame
	{\bfseries\sffamily} % Format of the whole section
	{} % Format of the section label
	{0cm} % Space between the title and label
	{#1} % Code before the label
	[] % Code after the label

\titlespacing*{\paragraph}{0pt}{0pt}{6pt} % Spacing around section titles, the order is: left, before and after

%----------------------------------------------------------------------------------------
%	TABLE OF CONTENTS
%----------------------------------------------------------------------------------------

\usepackage{titletoc} % Required for manipulating the table of contents

\setcounter{tocdepth}{2} % Display down to subsections in the table of contents

\contentsmargin{0cm} % Removes the default right margin

%------------------------------------------------

% Styling of numbered parts in the table of contents
\newcommand{\tocentrypartnumbered}[1]{%
	\setlength\fboxsep{0pt}% Remove box padding
	\contentslabel[%
		% Part number box
		\colorbox{ocre!20}{% Background color
			\strut\parbox[c][.7cm]{1.1cm}{% Box size
				\color{ocre!70}\Large\sffamily\bfseries\centering\thecontentslabel% Part number
			}%
		}%
		\hspace{4pt}%
		% Part title box
		\colorbox{ocre!40}{% Background color
			\strut\parbox[c][.7cm]{\linewidth-1.25cm}{% Box size
				\centering\Large\sffamily #1% Part title
			}%
		}%
	]{1.25cm}
}

% Styling of unnumbered parts in the table of contents
\newcommand{\tocentrypartunnumbered}[1]{%
	\setlength\fboxsep{0pt}% Remove box padding
	\contentslabel[%
		% Part title box
		\colorbox{ocre!40}{% Background color
			\strut\parbox[c][.7cm]{\linewidth}{% Box size
				\centering\Large\sffamily #1% Part title
			}%
		}%
	]{1.25cm}
}

\titlecontents{part} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{20pt}\Large\sffamily\bfseries\hypersetup{linkcolor=black}} % Before code
	{\tocentrypartnumbered} % Formatting of numbered sections of this type
	{\tocentrypartunnumbered} % Formatting of numberless sections of this type
	{} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{chapter} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{12pt}\large\sffamily\bfseries\hypersetup{linkcolor=ocre}} % Before code
	{\color{ocre}\contentslabel[\Large\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{\color{ocre!60}\normalsize\;\titlerule*[6pt]{.}\;\color{ocre}\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{section} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{3pt}\sffamily\bfseries} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~{\normalfont\titlerule*[6pt]{.}}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{subsection} % Section type being modified
	[1.25cm] % Left indentation
	{\addvspace{1pt}\sffamily\small} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code
	
%------------------------------------------------

\titlecontents{subsubsection} % Section type being modified
	[1.75cm] % Left indentation
	{\sffamily\small} % Before code
	{\contentslabel[\thecontentslabel]{1.75cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

% List of figures entries
\titlecontents{figure} % Section type being modified
	[0cm] % Left indentation
	{\addvspace{2pt}\sffamily\small} % Before code
	{\thecontentslabel\hspace*{1em}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

% List of tables entries
\titlecontents{table} % Section type being modified
	[0cm] % Left indentation
	{\addvspace{2pt}\sffamily\small} % Before code
	{\thecontentslabel\hspace*{1em}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~\titlerule*[6pt]{.}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number
	[] % After code

%------------------------------------------------

\titlecontents{lchapter} % Chapter headings on part pages
	[0cm] % Left indentation
	{\addvspace{12pt}\large\sffamily\bfseries\hypersetup{linkcolor=ocre}} % Before code
	{\color{ocre}\contentslabel[\Large\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{\color{ocre}} % Formatting of numberless sections of this type
	{~\color{ocre!60}\normalsize\titlerule*[6pt]{.}~\color{ocre}\thecontentspage} % Formatting of the filler to the right of the heading and the page number

%------------------------------------------------

\titlecontents{lsection} % Section headings on part pages
	[0cm] % Left indentation
	{\sffamily\small} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~{\normalfont\titlerule*[6pt]{.}}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number

%------------------------------------------------

\titlecontents{lsubsection} % Subsection headings on part pages
	[0cm] % Left indentation
	{\sffamily\footnotesize} % Before code
	{\contentslabel[\thecontentslabel]{1.25cm}\hspace{0.5cm}} % Formatting of numbered sections of this type
	{} % Formatting of numberless sections of this type
	{~{\normalfont\titlerule*[6pt]{.}}~\thecontentspage} % Formatting of the filler to the right of the heading and the page number

%----------------------------------------------------------------------------------------
%	BIBLIOGRAPHY
%----------------------------------------------------------------------------------------

% \usepackage[
% 	backend=biber, % Use the biber engine for compiling the bibliography
% 	bibstyle=numeric, % Main bibliography style
% 	citestyle=numeric, % In-text citation style
% 	sorting=nyt, % Sort references in the bibliography by name, then year, then title
% 	sortcites=true, % If multiple citekeys are passed to a citation command, sort them in the citation
% 	abbreviate=false, % Suppress abbreviations such as "Ed." for Editor
% 	backref=true, % List the page where references were cited in the bibliography
% 	defernumbers=true,
% ]{biblatex}

% \defbibheading{bibempty}{} % Suppress default bibliography headings

%----------------------------------------------------------------------------------------
%	INDEX
%----------------------------------------------------------------------------------------

\usepackage{makeidx} % Required to make an index

\makeindex % Tells LaTeX to create the files required for indexing

% Modify the command to output the index to output the correctly styled Index name to the page headers
\patchcmd{\theindex}
	{\MakeUppercase\indexname} % Find
	{\sffamily\normalsize\bfseries\indexname} % Replace
	{}
	{}

%----------------------------------------------------------------------------------------
%	 TABLES
%----------------------------------------------------------------------------------------

\usepackage{array} % Required for manipulating table elements

\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}} % Define a new right-aligned paragraph column type
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}} % Define a new left-aligned (no justification) paragraph column type
\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}} % Define a new centered paragraph column type

\usepackage{booktabs} % Required for high quality horizontal rules in tables

%----------------------------------------------------------------------------------------
%	 LISTS
%----------------------------------------------------------------------------------------

% \usepackage{enumitem} % Required for list customization
% \setlist{nolistsep, noitemsep} % Customize spacing inside and outside lists
% \renewcommand{\labelenumi}{\arabic{enumi}.} % Customize the first level numbered list characters
% \renewcommand{\labelenumii}{\alph{enumii}.} % Customize the second level numbered list characters
% \renewcommand{\labelenumiii}{\roman{enumiii}.} % Customize the third level numbered list characters
%------------------------------------------------
% 
% \renewcommand{\labelitemi}{\raisebox{-2pt}{\Large \textbullet}} % Customize the first level bullet point character
% \renewcommand{\labelitemii}{--} % Customize the second level bullet point character
% \renewcommand{\labelitemiii}{$\circ$} % Customize the third level bullet point character

%----------------------------------------------------------------------------------------
%	LINKS
%----------------------------------------------------------------------------------------

\RequirePackage[pdfusetitle]{hyperref}

% \hypersetup{
% 	colorlinks=true, % Whether to color links (a thin box is output around links if this is false)
% 	%hidelinks, % Hide the default boxes around links
% 	urlcolor=ocre, % Color for \url and \href links
% 	linkcolor=black, % Color for \ref/\nameref links
% 	citecolor=ocre, % Color for reference citations like \cite{}
% 	hyperindex=true, % Adds links from the page numbers in the index to the relevant page
% 	linktoc=all, % Link from section names and page numbers in the table of contents
% }

%----------------------------------------------------------------------------------------
%	BOOKMARKS
%----------------------------------------------------------------------------------------

\usepackage{bookmark} % Required for customizing PDF bookmarks

\bookmarksetup{
	open, % Open all bookmark drawers automatically
	numbered, % Add section numbers to bookmarks
	addtohook={%
		\ifnum\bookmarkget{level}=-1 % Customize part bookmarks
			\bookmarksetup{color=ocre, bold}% Bold and colored
		\fi
		\ifnum\bookmarkget{level}=0 % Customize chapter bookmarks
			\bookmarksetup{bold}% Bold
		\fi
	}
}

%----------------------------------------------------------------------------------------
%	TITLE PAGE
%----------------------------------------------------------------------------------------

\renewcommand{\titlepage}[2]{
	\thispagestyle{empty} % Suppress headers and footers on the title page

	\begin{tikzpicture}[remember picture, overlay]
		\node [inner sep=0pt] at (current page.center) {#1}; % Background image
		\node [anchor=center, inner sep=1.25cm, rectangle, fill=ocre!30!white, fill opacity=0.6, text opacity=1, minimum height=0.2\paperheight, minimum width=\paperwidth, text width=0.8\paperwidth] at (current page.center) {#2}; % Title highlight box with title(s) and author(s)
	\end{tikzpicture}
	
	\newpage
}

%----------------------------------------------------------------------------------------
%	THEOREM STYLES
%----------------------------------------------------------------------------------------

\usepackage{amsmath, amsfonts, amssymb, amsthm} % For math equations, theorems, symbols, etc

\renewcommand{\qedsymbol}{$\blacksquare$} % Redefine the QED symbol to be a filled square vs. the default unfilled square

%------------------------------------------------

% Orange theorem number and optional black title with padding above and below
\newtheoremstyle{ocrenum} % Theorem style name
	{6pt} % Space above
	{6pt} % Space below
	{\normalfont} % Body font
	{} % Indent amount
	{} % Theorem head font
	{} % Punctuation after theorem head
	{0.25em} % Space after theorem head
	{\small\sffamily\bfseries\color{ocre}\thmname{#1}~\thmnumber{\@ifnotempty{#1}{}\@upn{#2}} % Theorem text (e.g. Theorem 2.1)
	\thmnote{\the\thm@notefont\sffamily\bfseries\color{black}---~#3.\hspace{0.25em}}} % Optional theorem note

%------------------------------------------------

% Orange theorem number and optional black title with no padding above and below
\newtheoremstyle{ocrenumbox} % Theorem style name
	{0pt} % Space above
	{0pt} % Space below
	{\normalfont} % Body font
	{} % Indent amount
	{} % Theorem head font
	{} % Punctuation after theorem head
	{0.25em} % Space after theorem head
	{\small\sffamily\bfseries\color{ocre!80!black}\thmname{#1}~\thmnumber{\@ifnotempty{#1}{}\@upn{#2}} % Theorem text (e.g. Theorem 2.1)
	\thmnote{\the\thm@notefont\sffamily\bfseries\color{black}---~#3.\hspace{0.25em}}} % Optional theorem note

%------------------------------------------------

% Black theorem number and optional black title no padding above and below
\newtheoremstyle{blacknumex} % Theorem style name
	{6pt} % Space above
	{6pt} % Space below
	{\normalfont} % Body font
	{} % Indent amount
	{} % Theorem head font
	{} % Punctuation after theorem head
	{0.25em} % Space after theorem head
	{\small\sffamily\bfseries{\raisebox{1.25pt}{\tiny\ensuremath{\blacksquare}}}~\thmname{#1}~\thmnumber{\@ifnotempty{#1}{}\@upn{#2}} % Theorem text (e.g. Theorem 2.1)
	\thmnote{\the\thm@notefont\sffamily\bfseries---~#3.\hspace{0.25em}}} % Optional theorem note

%------------------------------------------------

% Black theorem number and optional black title padding above and below
\newtheoremstyle{blacknumbox} % Theorem style name
	{0pt} % Space above
	{0pt} % Space below
	{\normalfont} % Body font
	{} % Indent amount
	{} % Theorem head font
	{} % Punctuation after theorem head
	{0.25em} % Space after theorem head
	{\small\sffamily\bfseries\thmname{#1}~\thmnumber{\@ifnotempty{#1}{}\@upn{#2}} % Theorem text (e.g. Theorem 2.1)
	\thmnote{\the\thm@notefont\sffamily\bfseries---~#3.\hspace{0.25em}}} % Optional theorem note

%------------------------------------------------

\newcounter{counter}
\numberwithin{counter}{section}


% Orange theorem number and optional black title with padding above and below
\theoremstyle{ocrenum}


% Orange theorem number and optional black title with no padding above and below
\theoremstyle{ocrenumbox}
\newtheorem{propositionT}[counter]{Fakt} % Propositions, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{theoremeT}[counter]{Twierdzenie} % Theorems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{problem}{Problem}[chapter] % Problems, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{exerciseT}{Exercise}[chapter] % Exercises, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)

% Black theorem number and optional black title no padding above and below
\theoremstyle{blacknumex}
\newtheorem{exampleT}[counter]{Przyk\l{}ad} % Examples, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{notation}{Notation}[chapter] % Notations, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{vocabulary}{Vocabulary}[chapter] % Vocabularies, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)

% Black theorem number and optional black title with padding above and below
\theoremstyle{blacknumbox}
\newtheorem{definitionT}[counter]{Definicja} % Definitions, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1)
\newtheorem{corollaryT}[counter]{Wniosek} % Corollaries, the first argument is the theorem name, the second the theorem title used before the number and the third optional argument is whether to number under chapters (e.g. 2.1) or sections (e.g. 2.1.1


%----------------------------------------------------------------------------------------
%	COLORED THEOREM BOXES
%----------------------------------------------------------------------------------------

\RequirePackage[framemethod=default]{mdframed} % Required for creating colored boxes used for theorems, definitions, exercises and corollaries

% Theorem box
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	backgroundcolor=black!5, % Background color
	linecolor=ocre, % Border color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{tBox}

% Exercise box
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=ocre, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=ocre!10, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{eBox}

% Definition box
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=ocre, % Border color
	linewidth=4pt, % Border width
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=0pt, % Inside top margin height
	innerbottommargin=0pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{dBox}

% Corollary box
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=gray, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=black!5, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{cBox}


% Corollary box
\newmdenv[
	skipabove=7pt, % Whitespace above box
	skipbelow=7pt, % Whitespace below box
	rightline=false, % Right line visible
	leftline=true, % Left line visible
	topline=false, % Top line visible
	bottomline=false, % Bottom line visible
	linecolor=ocre, % Line color
	linewidth=4pt, % Line width
	backgroundcolor=ocre!5, % Background color
	innerleftmargin=5pt, % Inside left margin width
	innerrightmargin=5pt, % Inside right margin width
	innertopmargin=5pt, % Inside top margin height
	innerbottommargin=5pt, % Inside bottom margin height
	leftmargin=0cm, % Outside left margin width
	rightmargin=0cm % Outside right margin width
]{cpropBox}

% Creates an environment for each type of theorem and assigns it a theorem text style from the THEOREM STYLES block above and a colored box from above

\newenvironment{dupaexercise}{\begin{eBox}\begin{exerciseT}}{\hfill{\color{ocre}\tiny\ensuremath{\blacksquare}}\end{exerciseT}\end{eBox}}


\newenvironment{definition}{\begin{dBox}\begin{definitionT}}{\end{definitionT}\end{dBox}}
\newenvironment{example}{\begin{exampleT}}{\hfill{\tiny\ensuremath{\blacksquare}}\end{exampleT}}	
\newenvironment{theorem}{\begin{tBox}\begin{theoremeT}}{\end{theoremeT}\end{tBox}}
\newenvironment{corollary}{\begin{cBox}\begin{corollaryT}}{\end{corollaryT}\end{cBox}}
\newenvironment{proposition}{\begin{cpropBox}\begin{propositionT}}{\end{propositionT}\end{cpropBox}}

\theoremstyle{plain}
\numberwithin{counter}{section}
\newtheorem{conjecture}[counter]{Hipoteza}
\newtheorem{lemma}[counter]{Lemat}
\newtheorem{warning}[counter]{Uwaga}
\newtheorem{tobedone}[counter]{Wymaga przeredagowania}

%----------------------------------------------------------------------------------------
%	REMARK ENVIRONMENT
%----------------------------------------------------------------------------------------

\newenvironment{remark}{%
	\par\small % Reduce font size for remarks
	\vspace{4pt} % Vertical whitespace
	\begin{adjustwidth}{35pt}{25pt} % Left and right padding
		\hspace{-2.5pt}%
		\begin{tikzpicture}[overlay]
			\node[draw=ocre!60,line width=1pt,circle,fill=ocre!25,font=\sffamily\bfseries,inner sep=3pt,outer sep=0pt] at (-15pt,0pt){\textcolor{ocre}{R}}; % Orange R in a circle
		\end{tikzpicture}
	\advance\baselineskip -1pt% Reduce line spacing
}{%
	\end{adjustwidth}
}

%----------------------------------------------------------------------------------------
%	 LOAD PACKAGES THAT CLASH WITH OTHER PACKAGES
%----------------------------------------------------------------------------------------

\usepackage{tikz} % Required for drawing custom shapes and positioning elements absolutely on the page







% Book information for PDF metadata, remove/comment this block if not required 
\hypersetup{
	pdftitle={Title}, % Title field
	pdfauthor={Author}, % Author field
	pdfsubject={Subject}, % Subject field
	pdfkeywords={Keyword1, Keyword2, ...}, % Keywords
	pdfcreator={LaTeX}, % Content creator field
}

% \addbibresource{sample.bib} % Bibliography file

\definecolor{ocre}{RGB}{255, 105, 180} % Define the color used for highlighting throughout the book

\chapterimage{orange1.jpg} % Chapter heading image
\chapterspaceabove{6.5cm} % Default whitespace from the top of the page to the chapter title on chapter pages
\chapterspacebelow{6.75cm} % Default amount of vertical whitespace from the top margin to the start of the text on chapter pages

% \NeedsTeXFormat{LaTeX2e}
% \ProvidesClass{createspace}[2022/01/20 Create Space class]
% \LoadClass[twoside, 9pt]{extbook}

% to handle ą, ć, ę, etc.
\RequirePackage[utf8]{inputenc}
\RequirePackage[T1]{fontenc}
\RequirePackage{polski}

% to make the text as compact as possible
\usepackage{Alegreya}
% \RequirePackage[final]{microtype}
% \RequirePackage[compact]{titlesec}
\RequirePackage{paralist}



\RequirePackage{fancyhdr}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyfoot[C]{}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\pagestyle{fancy}
\fancyhead{}
\fancyfoot{}
% 341      Rozdział 7. Kalifat algebry | 7.2 Pierścień adeli              342 |
\fancyhead[LE]{\thepage}
\fancyhead[RE]{\nouppercase{\leftmark}}
\fancyhead[LO]{\nouppercase{\rightmark}}
\fancyhead[RO]{\thepage}
\renewcommand{\headrulewidth}{0.4pt}
\renewcommand{\footrulewidth}{0.0pt}

% https://tex.stackexchange.com/questions/22012/hyperref-and-imakeidx-do-not-work-together
\RequirePackage{imakeidx}

% \DeclareMathOperator:
\RequirePackage{amsmath}
% \mathbb:
\RequirePackage{amssymb}
% \theoremstyle, \newtheorem:
\RequirePackage{amsthm}
% [H] for figure environment:
\RequirePackage{float}
% \subcaption for minipage inside figure:
\RequirePackage{subcaption} % captions to subfigures
% clickable links
% add [backref] for links from bib entries to citations
% add [pdfusetitle] for metadata
\hypersetup{
    colorlinks,
    linkcolor={red!50!black},
    citecolor={blue!50!black},
    urlcolor={blue!80!black}
}



% https://www.reddit.com/r/LaTeX/comments/athzn1/replacing_leq_and_geq_with_leqslant_and_geqslant/
\let\savedleq=\leq %
\let\savedgeq=\geq %
\let\le=\leqslant %
\let\ge=\geqslant %

\input{00-meta-latex/shortcuts}






\usepackage{comment}
\includecomment{comment}

\makeindex[title=Skorowidz]
\makeindex[name=persons,title=Indeks osób]

\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{longtable}
\usepackage[table]{xcolor}
\usepackage[colorinlistoftodos,prependcaption]{todonotes}
\usepackage{tikz}
\usetikzlibrary{arrows.meta}
\usetikzlibrary{decorations.markings}
\usetikzlibrary{decorations.pathreplacing}
\usetikzlibrary{knots}
\colorlet{darkblue}{blue!80!black}
\definecolor{diagramfiller}{RGB}{255, 182, 193} % HTML: LightPink
\definecolor{first_colour}{RGB}{255, 105, 180}
\input{00-meta-latex/diagrams}

\definecolor{hotpink}{RGB}{255, 105, 180}
\definecolor{mediumvioletred}{RGB}{199, 21, 133}
\let\oldtabular\tabular % alternate rowcolors for all tables
\let\endoldtabular\endtabular
\renewenvironment{tabular}
{\rowcolors{2}{white}{hotpink}\oldtabular}
{\endoldtabular}
\let\oldlongtable\longtable % alternate rowcolors for all long-tables
\let\endoldlongtable\endlongtable
\renewenvironment{longtable}
{\rowcolors{2}{white}{hotpink}\oldlongtable}
{\endoldlongtable}

\hypersetup{
    colorlinks,
    linkcolor={mediumvioletred},
    citecolor={mediumvioletred},
    urlcolor={mediumvioletred}
}

\author{Casimir Allard}
\title{Kombinatoryczna teoria węzłów}
