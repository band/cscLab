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
      (insert "\n" line3 "\n" line2))
    (save-excursion
      (goto-char start)
      (while (re-search-forward "\\*\\*" end t)
        (replace-match "")))))
