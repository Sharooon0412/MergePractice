var player; //YouTube撥放器
var currentPlay = 0;//紀錄目前撥到第幾首

//當Youtube API準備好時
function onYouTubeIframeAPIReady(){ 
    //console.log("Hi");
    player = new YT.Player("player",
        {
            height:"390",
            width:"640",
            videoId:playList[currentPlay],
            playerVars:{
                "autoplay":0, //不自動播放
                "controls":0, //不顯示控制項
                "start":playTime[currentPlay][0], //起始秒數
                "end":playTime[currentPlay][1], //結束秒數
                "showinfo":0, //180925廢除(還是會顯示上方標題)
                "rel":0, //同上(可透過預載影片擋住)
                "iv_load_policy":3 //不顯示影片註解式行銷
            },
            events:{
                "onReady":onPlayerReady, //onReady時呼叫後方函式
                "onStateChange":onPlayerStateChange
            }
        }
    );
}

//當Youtube播放器準備好時
function onPlayerReady(event){
    $("#playButton").click
    (
        function()
        {
            $("#name").text(player.getVideoData().title);
            player.playVideo();
        }
    );
 }

//當播放器播放狀態轉變時
function onPlayerStateChange(event){ 
    $("#name").text(player.getVideoData().title);
    //console.log(event);
    //當目前播放秒數與預期播放結束秒數相同時 去撥下一首
    if(Math.floor(player.getCurrentTime())==playTime[currentPlay][1]){
        //正常播放下一首
        if(currentPlay<playList.length-1){
            currentPlay++;
            player.loadVideoById({
                "videoId":playList[currentPlay],
                "startSeconds":playTime[currentPlay][0],
                "endSeconds":playTime[currentPlay][1],
                "suggestedQuality":"large"
            });
        }else{ //已經撥到最後一首的話 就將第一首準備好 並停止播放
            currentPlay = 0;
            player.cueVideoById({
                "videoId":playList[currentPlay],
                "startSeconds":playTime[currentPlay][0],
                "endSeconds":playTime[currentPlay][1],
                "suggestedQuality":"large"
            });
        }
        //影片開始時抓取影片標題來顯示
        if(player.getVideoLoadedFraction()>0){
            $("#name").text(player.getVideoData().title);
        }
    }
}

