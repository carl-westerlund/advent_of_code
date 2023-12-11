import Data.Char (ord)
import Data.List (intersect, nub)

main = interact((++ "\n") . show . solve . readInput)

readInput :: String -> [(String, String)]
readInput = map split . lines
    where split s = splitAt (length s `div` 2) s

solve :: [(String, String)] -> Int
solve = sum . map (priority . commonItem)
    where commonItem (x,y) = nub $ x `intersect` y
          priority [c]
            | c `elem` ['a'..'z'] = ord c - ord 'a' + 1
            | c `elem` ['A'..'Z'] = ord c - ord 'A' + 27
