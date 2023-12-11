import Data.Char
import Data.List

main = interact ((++ "\n") . show . solve)

solve :: String -> Int
solve = (4+) . length . takeWhile (\x -> length x < 4) . map (nub . take 4) . tails
