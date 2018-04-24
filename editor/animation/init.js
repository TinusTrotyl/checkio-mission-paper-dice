//Dont change it
requirejs(['ext_editor_io', 'jquery_190', 'raphael_210'],
    function (extIO, $, TableComponent) {

        function paperDiceCanvas(dom, input) {
            const SIZE = 35;
            const
                color = {
                    dark: "#294270",
                    empty: "#FFFFFF",
                    unknown: "#8FC7ED",
                    filled: "#308AC0",
                },
                attr = {
                    rect_face: {
                        'stroke': color.dark,
                        'stroke-width': 1
                    },
                    rect_empty: {
                        'stroke': color.unknown,
                        'stroke-width': 1
                    },
                };
            const paper = Raphael(dom,
                             input[0].length * SIZE + 3, 
                             input.length * SIZE + 3,
                             0, 0);
            
            for (let y=0; y < input.length; y += 1) {
                for (let x=0; x < input[0].length; x += 1) {

                    //Dots
                    const n = parseInt(input[y].substr(x, 1), 10);
                    const rt = paper.rect(x * SIZE + 1, y * SIZE + 1,
                        SIZE, SIZE
                        ).attr(n ? attr.rect_face: attr.rect_empty);
                    if (n) {
                        rt.toFront();
                    } else {
                        rt.toBack();
                    }

                    //corners
                    const r = 3;
                    const attrDot = {
                        "stroke-width": 0, 
                        "fill": color.dark
                    };
                    const cx = x * SIZE + 4;
                    const cy = y * SIZE + 4;
                    if (n % 2 === 1) {
                        paper.circle(cx+r*5, cy+r*5, r).attr(attrDot);
                    }
                    if (n > 1) {
                        paper.circle(cx+r*2, cy+r*2, r).attr(attrDot);
                        paper.circle(cx+r*8, cy+r*8, r).attr(attrDot);
                    }
                    if (n > 3) {
                        paper.circle(cx+r*2, cy+r*8, r).attr(attrDot);
                        paper.circle(cx+r*8, cy+r*2, r).attr(attrDot);
                    }
                    if (n === 6) {
                        paper.circle(cx+r*2, cy+r*5, r).attr(attrDot);
                        paper.circle(cx+r*8, cy+r*5, r).attr(attrDot);
                    }
                }
            }
        }

        let $tryit;
        let io = new extIO({
            multipleArguments: false,
            functions: {
                js: 'paperDice',
                python: 'paper_dice'
            },
            animation: function($expl, data){
                paperDiceCanvas(
                    $expl[0],
                    data.in
                );
            }
        });
        io.start();
    }
);
