import Data.Char (ord)
import Data.List (intersect, nub)
import Data.List.Split (chunksOf)

main = interact((++ "\n") . show . solve . readInput)

readInput :: String -> [[String]]
readInput = chunksOf 3 . lines

solve :: [[String]] -> Int
solve = sum . map (priority . commonItem)
    where commonItem = nub . foldl1 intersect
          priority [c]
            | c `elem` ['a'..'z'] = ord c - ord 'a' + 1
            | c `elem` ['A'..'Z'] = ord c - ord 'A' + 27
