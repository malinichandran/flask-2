
    function starOutGrid(grid){
        let row; 
        let col;
        
        for(let i=0; i<grid.length; i++){
         
            for(let j=0; j<grid[0].length; j++){
          if(grid[i][j]==='*'){
            row=i;
            col=j;
            
           }
          }
          
        }
        if(row!=="undefined"){
        for(let j=0;j<grid.length;j++){
            grid[row][j]="*";
        }
        for(let i=0;i<grid[0].length;i++){
            grid[i][col]="*";
        }
        }
        
        return grid;
        } 
        

