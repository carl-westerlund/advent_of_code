import Data.List.Split (splitOneOf)

main = interact((++ "\n") . show . solve . readInput)

readInput :: String -> [((Int, Int), (Int, Int))]
readInput = map (split . splitOneOf "-,") . lines
    where split [a,b,x,y] = ((read a, read b), (read x, read y))

solve :: [((Int, Int), (Int, Int))] -> Int
solve = length . filter overlap
    where overlap ((a,b),(s,t)) = b >= s && t >= a
