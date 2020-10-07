## Motivation

* Understanding & implementing workflows is hard
* We provide a guide to one alternative, 'Snakemake'

* Practical Example: Replicating Mankiw, Romer & Weil's 1992 QJE

## Another slide

* Bullets
    - Sub bullets
    - *italic*
    - **bold**

1. Numbered Lists ...
2. Can go like this

## Adding a Table

## Adding a Figure

\begin{figure}[h!]
        \centering
        \caption{\small{Caption for Entire Figure}}
        \includegraphics[width=0.75\textwidth]{out/figures/unconditional_convergence.pdf}
        \label{fig:main_fig}
\begin{fignote}
    \textit{Notes}: Here are some Figure notes.
\end{fignote}
\end{figure}

## Adding Subfigure

\begin{figure}[h!]
        \centering
        \caption{\small{Caption for Entire Figure}}
        \begin{subfigure}[b]{0.475\textwidth}
            \centering
            \includegraphics[width=\textwidth]{out/figures/unconditional_convergence.pdf}
            \caption{\small{Fig A}}
            \label{fig:fig_a}
        \end{subfigure}
        \hfill
        \begin{subfigure}[b]{0.475\textwidth}
            \centering
            \includegraphics[width=\textwidth]{out/figures/conditional_convergence.pdf}
            \caption{\small{Fig B}}
            \label{fig:fig_b}
        \end{subfigure}
        \vskip\baselineskip
        \begin{subfigure}[b]{0.475\textwidth}
            \centering
            \includegraphics[width=\textwidth]{out/figures/aug_conditional_convergence.pdf}
            \caption{\small{Fig C}}
            \label{fig:fig_c}
        \end{subfigure}
        \hfill
        \label{fig:main_subfig}
\begin{fignote}
    \textit{Notes}: Here are some Figure notes.
\end{fignote}
\end{figure}
