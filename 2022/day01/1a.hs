import Data.List
import Data.Function (on)

main = interact $ (++ "\n") . show . solve . readInput

readInput :: String -> [[Int]]
readInput = map (map read) . groupLn . lines
    where groupLn = filter (not . any null) . groupBy ((==) `on` null)

solve :: [[Int]] -> Int
solve = maximum . map sum
