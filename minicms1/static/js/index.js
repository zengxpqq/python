/**
 * Main JS file for Casper behaviours
 */

/* globals jQuery, document */
(function ($, undefined) {
    "use strict";
    var $document = $(document);
    $document.ready(function () {

        //导航按钮 set menu-button
        $(".menu-button, .nav-close").on("click", function(e){
            e.preventDefault();
            $("body").toggleClass("nav-opened nav-closed");
        });

        //获取当前地址
        var curUrl=window.location.href;

        //指定语言按钮的地址 set the language url
        var curUrlGroup=curUrl.split("/");        
        curUrl="";     
        for(var i=3;i<curUrlGroup.length;i++){            
            curUrl+="/"+curUrlGroup[i];
        };
        var enUrl="http://www.base-fx.com"+curUrl; 
        var cnUrl="http://cn.base-fx.com"+curUrl; 
        $(".cn").attr("href",cnUrl);
        $(".en").attr("href",enUrl);        

        //窗口变化后自适应
        window.onresize=function(){
            resizeVid();   //showreel自适应
            $(".showBox").height($(".showBox").width()/2.2);   //首页图片自适应
        }

               //视频按照父级比例自动适应
        var $videoContainer = $(".video");
        var $videoPlayer = $(".video-js");
        if ($videoContainer.length>0){//如果reel视频存在
            //setVid();  //设置reel视频，视频暂停显示播放大按钮
            resizeVid(); //初始化reel视频大小
        }       
        function setVid(){//视频暂停显示播放大按钮
            $videoPlayer.each(function(){
                var myPlayer = videojs($(this).attr("id"));
                myPlayer.on("pause",function(){  
                    this.controlBar.hide();              
                    this.bigPlayButton.show();
                    this.on("play",function(){  
                        this.controlBar.show();              
                       this.bigPlayButton.hide();
                    });
                });
            });
        }        
        function resizeVid(){//showreel自动适应屏幕大小
            $videoContainer.each(function(){
                var videoNewH = $(this).parent().width()/(1280/695);
                if ( $(this).hasClass("feature-reel") ) {
                   $(this).width("97.3%"); 
                   $(this).height($(this).parent().width()/(1280/695)); 
                }else if ( $(this).hasClass("reel") && $(window).width()<500 ) {
                   $(this).width("97.3%"); 
                   $(this).height($(this).parent().width()/(1280/695)); 
                }else if ($(this).hasClass("reel")){
                   $(this).width("31%"); 
                   $(this).height( ($(this).parent().width()*0.31)/(1280/695) ); 
                }  
                $(this).show();
            });
        }



        //首页读取内容  
        function changeTo(num){//首页图片切换函数
            $(".showImg ul li").removeClass("imgOn").fadeOut(fadeTime*1000).eq(num).fadeIn(fadeTime*1000).addClass("imgOn");
            $(".showIndex li").css("background","#999").eq(num).css("background","#fff");
        };      
        if ( $(".showImg").length>0 ){//读取首页大图片
            $(".showImg").load("/home/ .featureImgs",function(){
                for(var i=0;i< $(".showImg li").length;i++){
                    $(".showIndex").append("<li></li>")
                }
                $(".showIndex li").each(//鼠标点击导航圆点
                    function(item){
                        $(this).click(function(){
                            clearInterval(autoChange);
                            curIndex = item;
                            changeTo(curIndex);
                            autoChange = setInterval(function(){            
                               if(curIndex < $(".showImg li").length-1){
                                    curIndex ++;
                                }else{
                                    curIndex = 0;
                                }
                                changeTo(curIndex);         
                                },intervalTime*1000);
                            }                    
                         );
                    }
                ); 
                
            }); 

            //图片轮播代码    
            $(".showBox").height($(".showBox").width()/2.2);//初始化图片轮换的高度
            var intervalTime=3.5;  //轮播切换间隔时间
            var fadeTime=1;//渐显时间
            var  curIndex = 0;//当前图片索引0             
            var autoChange = setInterval(function(){  //自动间隔切换函数          
                if(curIndex < $(".showImg ul li").length-1){
                    curIndex ++;
                }else{
                    curIndex = 0;
                }                
                changeTo(curIndex);         
            },intervalTime*1000);            
                   
        } ;
        if ( $(".welcome").length>0 ){//获取欢迎话语
            $(".welcome").load("/home/ .welcome-content");
        }  
        if ( $(".home-reel").length>0 ){//获取首页reel视频
            $("<video></video>").load("/home/ .reel-content",function(){
                $(".home-reel").append('<script type="text/javascript" src="assets/js/video-js/video.js"></script>'+$(this).html());   
                var $videoPlayer = $(".video-js");
                setVid();    
                function setVid(){//视频暂停显示播放大按钮
                    $videoPlayer.each(function(){
                        var myPlayer = videojs($(this).attr("id"));
                        myPlayer.on("pause",function(){  
                            this.controlBar.hide();              
                            this.bigPlayButton.show();
                            this.on("play",function(){  
                                this.controlBar.show();              
                               this.bigPlayButton.hide();
                            });
                        });
                    });
                } 
            });
        }
        if ( $(".listShows ul").length>0 ){//获取首页reel视频
             $(".listShows ul").load("/shows/ .latest");//读取最新的show
        }


        //news页面,瀑布流代码,首页引用了imagesloaded和mousewheel插件
        var $gridContainer = $(".loop-content");
        if($gridContainer.length>0){//如果是在新闻页             
            $gridContainer.imagesLoaded(function(){//全部图片读取完毕后执行
                $gridContainer.fadeIn(500);
                $gridContainer.masonry({//瀑布流布局新闻块
                    itemSelector:".loop",
                    isResizable:true,
                    isAnimated:true,
                });
            });
            var curPage=1; //定义当前页码，默认1 
            var pageTotal=parseInt($(".page-number").html().substr(10)); //获取总页数
            var pageUrl = "/tag/news/page/"+(curPage+1)+" .loop" ; //获取下一页地址 
            try {//判断是否支持触控
                document.createEvent("TouchEvent");
                document.addEventListener("touchend",goLoad,false);                 
            } catch(err){    
                document.addEventListener("scroll",goLoad,false);   
            }                         
        }  
        function goLoad(){
            var scrollTop = $(document).scrollTop();   
            if (  scrollTop >= ($(document).height()-$(window).height()-10) && curPage<pageTotal ){                     
                $(".loadInfo").html("Loading...").fadeIn(300);  
                loadGrid();  
            }else if (  scrollTop >= ($(document).height()-$(window).height()) && curPage>=pageTotal ){
                $(".loadInfo").html("No more post.").fadeIn(300);                                        
            }else{
                $(".loadInfo").fadeOut(300);
            } 
        }  
        function loadGrid(){//加载下一页函数             
            pageUrl = "/tag/news/page/"+(curPage+1)+" .loop" ;
            $("<div></div>").load(pageUrl,function(){                    
                var $newElems = $(this);       
                $newElems.imagesLoaded(function(){                     
                    $(".loadInfo").fadeOut(300);                        
                    $gridContainer.append($newElems).masonry("appended",$newElems,true);                                                               
                    tranTo();//读取新的内容翻译成简繁体
                }); 
            }); 
            curPage++;                                            
        };   


        //设置shows页面的时间线对称 set shows page timeline mirror
        if($(".listShows-content").length>0){
            $(".year:odd").addClass("mirror"); 
            $(".listShows-content").show(500);
        }

        //About 页面主要成员点击显示资料
        if($(".profile").length>0){           
            $(".profile").click(
                function(){
                    if( $(this).hasClass(".profile_On")){
                        $(this).parent().find(".profile").find("p").slideUp(200);
                        $(this).removeClass(".profile_On");
                    }else{
                        $(this).parent().find(".profile").find("p").slideUp(200);
                        $(this).parent().find(".profile").removeClass(".profile_On");
                        $(this).find("p").slideDown(200);
                        $(this).addClass(".profile_On")
                    }                    
               }        
            ); 
        }
        
        if( $(".page-sider.sider").length>0){  //如果有侧边栏加载 
            $(".page-sider.sider").load("/sider/ .adv");
        }
        

        //contact 页面滚动到指定的ID
        if( $(".office-title").length>0 ){
            $(".office-title").click(function(){
                var goToId = $(this).index()+1;
                $("html,body").animate({scrollTop:$("#office-"+goToId).offset().top},500);
            });
        }

        //set cast 职员表
        if( $(".cast").length>0 ){
            $(".cast").click(function(){
                $(".cast-content").slideToggle(500);
            });
        }      

        //简历提交页面代码
        //Job portal page add Experience
        var expirenceNum=0;
        var experienceContent=$("#experience").html();
        var experienceTotol=3;
        $("#addExperirence").click(function(){    
            experienceContent=experienceContent.replace("experience-"+expirenceNum,"experience-"+(expirenceNum+1)).replace("experienceIndex-"+expirenceNum,"experienceIndex-"+(expirenceNum+1)).replace(expirenceNum+"Name",expirenceNum+1+"Name").replace(expirenceNum+"Period",expirenceNum+1+"Period").replace(expirenceNum+"QuitReason",expirenceNum+1+"QuitReason").replace(expirenceNum+"WorkContent",expirenceNum+1+"WorkContent");
            $("#experience").append(experienceContent);
            $("#experience").find("#experienceIndex-"+(expirenceNum+1)).slideDown(500);
            expirenceNum++;
            if( expirenceNum>0 && expirenceNum<experienceTotol ){
                $("#subExperirence").show(100);
            }else{
                $("#addExperirence").hide(100);
            }
        });
        $("#subExperirence").click(function(){   
            if( expirenceNum==0 ){       
            }else{        
                experienceContent=experienceContent.replace("experience-"+expirenceNum,"experience-"+(expirenceNum-1)).replace("experienceIndex-"+expirenceNum,"experienceIndex-"+(expirenceNum-1)).replace(expirenceNum+"Name",expirenceNum-1+"Name").replace(expirenceNum+"Period",expirenceNum-1+"Period").replace(expirenceNum+"QuitReason",expirenceNum-1+"QuitReason").replace(expirenceNum+"WorkContent",expirenceNum-1+"WorkContent");
                $("#experience").find("#experienceIndex-"+expirenceNum).slideUp(500,function(){
                    $(this).remove();
                });
                expirenceNum--;
                if( expirenceNum==0 ){
                    $("#subExperirence").hide(100);
                }else{
                    $("#addExperirence").show(100);
                }
            }     
        });
        //Job portal page add education
        var educationNum=0;
        var educationContent=$("#education").html();
        var educationTotol=3;
        $("#addEducation").click(function(){    
            educationContent=educationContent.replace("education-"+educationNum,"education-"+(educationNum+1)).replace("educationIndex-"+educationNum,"educationIndex-"+(educationNum+1)).replace(educationNum+"Name",educationNum+1+"Name").replace(educationNum+"Period",educationNum+1+"Period").replace(educationNum+"QuitReason",educationNum+1+"QuitReason").replace(educationNum+"WorkContent",educationNum+1+"WorkContent");
            $("#education").append(educationContent);
           $("#education").find("#educationIndex-"+(educationNum+1)).slideDown(500);
            educationNum++;
            if( educationNum>0 && educationNum<educationTotol ){
                $("#subEducation").show(100);
            }else{
                $("#addEducation").hide(100);
            }
        });
        $("#subEducation").click(function(){   
            if( educationNum==0 ){       
            }else{        
                educationContent=educationContent.replace("education-"+educationNum,"education-"+(educationNum-1)).replace("educationIndex-"+educationNum,"educationIndex-"+(educationNum-1)).replace(educationNum+"Name",educationNum-1+"Name").replace(educationNum+"Period",educationNum-1+"Period").replace(educationNum+"QuitReason",educationNum-1+"QuitReason").replace(educationNum+"WorkContent",educationNum-1+"WorkContent");
                $("#education").find("#educationIndex-"+educationNum).slideUp(500,function(){
                    $(this).remove();
                });
                educationNum--;
                if( educationNum==0 ){
                    $("#subEducation").hide(100);
                }else{
                    $("#addEducation").show(100);
                }
            }     
        });
        //Job portal page add Attachment
        var attachmentNum=0;
        var attachmentContent=$("#attachment").html();
        var attachmentTotol=10;
        $("#addAttachment").click(function(){    
            attachmentContent=attachmentContent.replace("attachment-"+attachmentNum,"attachment-"+(attachmentNum+1)).replace("attachmentIndex-"+attachmentNum,"attachmentIndex-"+(attachmentNum+1)).replace(attachmentNum+"Name",attachmentNum+1+"Name").replace(attachmentNum+"Period",attachmentNum+1+"Period").replace(attachmentNum+"QuitReason",attachmentNum+1+"QuitReason").replace(attachmentNum+"WorkContent",attachmentNum+1+"WorkContent");
            $("#attachment").append(attachmentContent);
            $("#attachment").find("#attachmentIndex-"+(attachmentNum+1)).slideDown(500);
            attachmentNum++;
            if( attachmentNum>0 && attachmentNum<attachmentTotol ){
                $("#subAttachment").show(100);
            }else{
                $("#addAttachment").hide(100);
            }
        });
        $("#subAttachment").click(function(){   
            if( attachmentNum==0 ){       
            }else{        
                attachmentContent=attachmentContent.replace("attachment-"+attachmentNum,"attachment-"+(attachmentNum-1)).replace("attachmentIndex-"+attachmentNum,"attachmentIndex-"+(attachmentNum-1)).replace(attachmentNum+"Name",attachmentNum-1+"Name").replace(attachmentNum+"Period",attachmentNum-1+"Period").replace(attachmentNum+"QuitReason",attachmentNum-1+"QuitReason").replace(attachmentNum+"WorkContent",attachmentNum-1+"WorkContent");
                $("#attachment").find("#attachmentIndex-"+attachmentNum).slideUp(500,function(){
                    $(this).remove();
                });
                attachmentNum--;
                if( attachmentNum==0 ){
                    $("#subAttachment").hide(100);
                }else{
                    $("#addAttachment").show(100);
                }
            }     
        });
        
       
        

        



    });
})(jQuery);









     

    
   