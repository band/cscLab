
import git

repo = git.Repo("/Users/band/Sites/massivewiki/bandstands")

>>> repo
<git.repo.base.Repo '/Users/band/Sites/massivewiki/bandstands/.git'>

>>> repo.git.log('-n 3', '--numstat', '--pretty=%h--%ad')
# yields a string; need to split or something to get another data structure

repo.git.log('-n 3', '--numstat', '--name-only', '--pretty=tformat:').split('\n')
# yields a list, with one filename per item
