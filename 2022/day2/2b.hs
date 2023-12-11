import Data.Char (ord)

main = interact((++ "\n") . show . solve . readInput)

readInput :: String -> [(Int, Int)]
readInput = map (mkTuple . words) . lines
    where mkTuple [[x], [y]] = (ord x - ord 'A', ord y - ord 'X')

solve :: [(Int, Int)] -> Int
solve = sum . map score
    where score (x,y) = y*3 + ((x+y-1) `mod` 3 + 1)
