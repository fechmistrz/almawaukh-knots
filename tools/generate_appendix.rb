#!/usr/bin/env ruby

def one_entry(crossings, index)
    puts %q"\begin{minipage}[b]{.18\linewidth}"
    puts %q"\centering"
    puts "\\includegraphics[width=\\linewith]{../images/#{crossings}_#{index}.png}"
    puts "\\subcaption{$#{crossings}_{#{index}}$}"
    puts %q"\end{minipage}"
end

counter = 0
KNOTS = {
    3 => 1,
    4 => 1,
    5 => 2,
    6 => 3,
    7 => 7,
    8 => 21,
    9 => 49,
    10 => 165,
}

KNOTS.each {|crossings, max_index|
    (1..max_index).each {|index|
        puts %q"\begin{figure}" if counter % 5 == 0
        one_entry(crossings, index)
        counter = counter + 1
        if (counter % 5 == 0 && counter > 0)
            puts %q"\end{figure}"
            puts ""
        end
    }
}

puts %q"\end{figure}" if counter % 5 != 0