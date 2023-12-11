import Data.List
import Data.List.Split
import Data.Char

main = interact((++ "\n") . show . solve . readInput)

readInput :: String -> ([String], [(Int, Int, Int)])
readInput s =
    let [labeledStacks, instructions] = splitOn [""] $ lines s
        (stacksData, [labels]) = splitAt (length labeledStacks - 1) labeledStacks
        stacks = map reverse . filter (any isUpper) . map (filter $ not . isSpace) . transpose . reverse $ stacksData
    in (stacks, map (readInstr . words) instructions)
   where readInstr x = (read $ x !! 1, read (x !! 3) - 1, read (x !! 5) - 1)

solve :: ([String], [(Int, Int, Int)]) -> String
solve (stacks, instructions) = map head $ foldl moveCrates stacks instructions

moveCrates :: [String] -> (Int, Int, Int) -> [String]
moveCrates stacks (n, fr, to) =
    let (toMove, stay) = splitAt n (stacks !! fr)
     in [if i == fr then stay else if i == to then reverse toMove ++ (stacks !! to) else stacks !! i | i <- [0..(length stacks - 1)]]
