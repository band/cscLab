(defun modify-region ()
  "Remove '**' characters and move lines 2 and 3 to the bottom in the selected region."
  (interactive)
  (let ((start (region-beginning))
        (end (region-end))
        (line2 nil)
        (line3 nil))
    (save-excursion
      (goto-char start)
      (forward-line 1)
      (setq line2 (buffer-substring (point) (line-end-position)))
      (delete-region (point) (line-end-position))
      (forward-line 1)
      (setq line3 (buffer-substring (point) (line-end-position)))
      (delete-region (point) (line-end-position)))
    (save-excursion
      (goto-char end)
      (insert line2 "\n" line3))
    (save-excursion
      (goto-char start)
      (flush-lines "^\\s-*$")
      (while (re-search-forward "\\*\\*" end t)
        (replace-match "")))
      (save-excursion
	(goto-char start)
	(while (re-search-forward "^Year: \\([0-9]+\\)" nil t)
	  (replace-match "(\\1)")))
        (save-excursion
	  (goto-char (point-min))
	  (let ((line1 (buffer-substring-no-properties (line-beginning-position) (line-end-position)))
		(line2 (progn (forward-line 1) (buffer-substring-no-properties (line-beginning-position) (line-end-position)))))
	    (delete-region (point-min) (progn (forward-line 1) (point)))
	    (insert (concat line1 line2 "\n"))))
      ))
