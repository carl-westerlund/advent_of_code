import Data.Char
import Data.List

main = interact ((++ "\n") . show . solve)

solve :: String -> Int
solve = (14+) . length . takeWhile (\x -> length x < 14) . map (nub . take 14) . tails
