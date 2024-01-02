
        //$(document).ready(function () {
        //    for (var i = 0; i < indian.Length; i++) {
        //        var ExchCode = indian[i].index.exchange;
        //        var Sccode = indian[i].index.indexCode;
        //        SendToBServer(CreateScripDatabyExchCode(ExchCode, Sccode, "1"));
    
        //    }
        //});
    
        function callJSforHome() {
            for (var i = 0; i < indian.Length; i++) {
                var ExchCode = indian[i].index.exchange;
                var Sccode = indian[i].index.indexCode;
                SendToBServer(CreateScripDatabyExchCode(ExchCode, Sccode, "1"));
    
            }
        }
    
    
        function AssignACTArrow(exchange, indexCode)
        {
    
           // debugger
          //  alert('AssignACTArrow'); 
            var CPerValue = document.getElementById(exchange+indexCode+"CPer").innerHTML();
    
                            
        }
                          
        function PushDataToCleverTapForScrips(EventName, Indices, Scrips, Source) {
            try {
                clevertap.event.push(EventName, {
                    "Indices": Indices,
                    "Scrips": Scrips,
                    "Source": Source,
                    "Date": new Date()
                });
            }
            catch {
                createNetcoreLog(EventName + " | " + "_HomeIndianIndices.cshtml");
            }
        }
    
    
        var filterDropdown = 'ALL,NIFTY,BANKNIFTY,USDINR';
    
        var addInfo = filterDropdown.split(',');
        if (addInfo.length > 0) {
            $('#exampleFormControlSelect1').empty();
    
            //$('#DD_BankList').append("<option value='' selected>Select Bank</option>");
    
            for (var ii = 0; ii < addInfo.length; ii++) {
                {
                    $('#exampleFormControlSelect1').append("<option value='" + addInfo[ii] + "'>" + addInfo[ii] + "</option>");
                }
    
            }
    
        }
    
        //var ParentURL = 'http://localhost:5045/OptionDabbler/';
        //var ParentURL = 'http://uattrade.motilaloswal.com:8096/OptionDabbler/';
        var ParentURL = 'https://invest.motilaloswal.com/OptionDabbler/';
        $("#bestpot").hide();
        $("#predicttrade").hide();
        $("#opstrategy").hide();
    
        var OptionStrategies;
        var PotType = '';
        var MegaPot = 2;
        var FreePot = 1;
        var Starterid = 'Starter';
        var Startercondition = 'action=Buy|multileg=false';
        var Margin10Kid = 'Margin10K';
        var Margin10Kidcondition = 'requiredfunds=10000';
        var MaxLossId = 'MaxLoss2K';
        var MaxLossIdcondition = 'maxloss=2000';
        var StrategyMultileg = 'Strategy';
        var StrategyMultilegcondition = 'multileg=true';
        var OnlySellID = 'OnlySell';
        var OnlySellcondition = 'action=Sell|multileg=false';
        var OtherFreeOptions = '';
        var OtherFreeOptionslen = 0;
        var ajaxResult;
        var errorFlag;
        var IsFnOActivated = '';
        var IsCDActivated = '';
        var isMCXActivated = '';
        $(document).ready(function () {
            $("#bestpot").hide();
            $("#predicttrade").hide();
            $("#opstrategy").hide();
            IsFnOActivated = '' +'N'+'';
            IsCDActivated = ''+'N'+'';
            isMCXActivated = '' + '' + '';
            var niftyid = ''+'0'+'26000'+'';
            var bankniftyid = ''+'2'+'57919'+'';
            var usdinrid = '' + '3' + '3129' + '';
            var goldid = '' + '6' + '250883' + '';
    
            var PotType = MegaPot;
            OptionStoreCreateSession();
            $.ajax({
                type: "GET",
                url: "/Home/GetMegaFreeOptionStrategies?strategyPotType=" + PotType,
                async: false,
                contentType: 'application/json; charset=utf-8',
                dataType: "text",
                success: function (response) {
                    OptionStrategies = JSON.parse(response);
                    var Pots = JSON.parse(OptionStrategies).data.pots;
                   // console.log(OptionStrategies)
                    //debugger;
                    if (PotType == FreePot || Pots.length ==0) {
                        $("#bestpot").hide();
                        $("#predicttrade").hide();
                        $("#opstrategy").show();
                        $("#one").attr('checked', true);
    
                        LoadFreePotsOnHome("All", "Onload");
                        /*DashboardSTARTER(3);*/
                    }
                    else if (PotType == MegaPot) {
                        $("#MegaPots").html("");
                        $("#opstrategy").hide();
                        $("#predicttrade").hide();
                        var potHTML = '';
                        for (var i = 0; i < Pots.length; i++) {
    
                            //Pots[i].maxProfit = Math.round(Pots[i].maxProfit);
                            //Pots[i].requiredFunds = Math.round(Pots[i].requiredFunds);
                            //Pots[i].maxLoss = Math.round(Pots[i].maxLoss);
                            potHTML = potHTML + '<div class="wsection">';
                            potHTML = potHTML + '<div class="twoblock custwidth">';
                            potHTML = potHTML + '    <div class="column">';
                            potHTML = potHTML + '        <div class="leftmd">';
                            if (Pots[i].symbol == 'USDINR') {
                                potHTML = potHTML + '            <svg id="OptionUSDINRUp" class="mr10" data-name="trending_up_black_24dp (5)" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 69.351 69.351">';
                                potHTML = potHTML + '                <path data-name="Path 3164" d="m42.455 6 6.617 6.617-14.1 14.1-11.56-11.557L2 36.6l4.074 4.074 17.338-17.336L34.971 34.9l18.2-18.176 6.617 6.617V6z" transform="translate(3.779 11.338)" style="fill:#27bf6e"></path>';
                                potHTML = potHTML + '            </svg>';
                                potHTML = potHTML + '            <svg id="OptionUSDINRDown" class="mr10" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 32 20">';
                                potHTML = potHTML + '               <path data-name="Path 3636" d = "m11.6 26-3.664-3.817 7.808-8.133 6.4 6.667L34 8.35 31.744 6l-9.6 10-6.4-6.667-10.08 10.484L2 16v10z" transform = "translate(-2 -6)" style = "fill:#e10000" ></path >';
                                potHTML = potHTML + '            </svg >';
                                potHTML = potHTML + '            <span>' + Pots[i].symbol + ' <span class="medium OptionUSDINR ' + usdinrid + '" id="OptionUSDINR">0.0000</span></span>';
                            }
                            else if (Pots[i].symbol == 'BANKNIFTY') {
                                potHTML = potHTML + '            <svg id="OptionBANKNIFTYUp" class="mr10" data-name="trending_up_black_24dp (5)" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 69.351 69.351">';
                                potHTML = potHTML + '                <path data-name="Path 3164" d="m42.455 6 6.617 6.617-14.1 14.1-11.56-11.557L2 36.6l4.074 4.074 17.338-17.336L34.971 34.9l18.2-18.176 6.617 6.617V6z" transform="translate(3.779 11.338)" style="fill:#27bf6e"></path>';
                                potHTML = potHTML + '            </svg>';
                                potHTML = potHTML + '            <svg id="OptionBANKNIFTYDown" class="mr10" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 32 20">';
                                potHTML = potHTML + '               <path data-name="Path 3636" d = "m11.6 26-3.664-3.817 7.808-8.133 6.4 6.667L34 8.35 31.744 6l-9.6 10-6.4-6.667-10.08 10.484L2 16v10z" transform = "translate(-2 -6)" style = "fill:#e10000" ></path >';
                                potHTML = potHTML + '            </svg >';
                                potHTML = potHTML + '            <span>' + Pots[i].symbol + ' <span class="medium OptionBANKNIFTY ' + bankniftyid + '"  id="OptionBANKNIFTY">0.0000</span></span>';
                            }
                            else if (Pots[i].symbol == 'NIFTY') {
                                potHTML = potHTML + '            <svg id="OptionNIFTYUp" class="mr10" data-name="trending_up_black_24dp (5)" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 69.351 69.351">';
                                potHTML = potHTML + '                <path data-name="Path 3164" d="m42.455 6 6.617 6.617-14.1 14.1-11.56-11.557L2 36.6l4.074 4.074 17.338-17.336L34.971 34.9l18.2-18.176 6.617 6.617V6z" transform="translate(3.779 11.338)" style="fill:#27bf6e"></path>';
                                potHTML = potHTML + '            </svg>';
                                potHTML = potHTML + '            <svg id="OptionNIFTYDown" class="mr10" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 32 20">';
                                potHTML = potHTML + '               <path data-name="Path 3636" d = "m11.6 26-3.664-3.817 7.808-8.133 6.4 6.667L34 8.35 31.744 6l-9.6 10-6.4-6.667-10.08 10.484L2 16v10z" transform = "translate(-2 -6)" style = "fill:#e10000" ></path >';
                                potHTML = potHTML + '            </svg >';
                                potHTML = potHTML + '            <span>' + Pots[i].symbol + ' <span class="medium OptionNIFTY ' + niftyid + '" id="OptionNIFTY">0.0000</span></span>';
                            }
                            else if (Pots[i].symbol == 'GOLD') {
                                potHTML = potHTML + '            <svg id="OptionGoldUp" class="mr10" data-name="trending_up_black_24dp (5)" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 69.351 69.351">';
                                potHTML = potHTML + '                <path data-name="Path 3164" d="m42.455 6 6.617 6.617-14.1 14.1-11.56-11.557L2 36.6l4.074 4.074 17.338-17.336L34.971 34.9l18.2-18.176 6.617 6.617V6z" transform="translate(3.779 11.338)" style="fill:#27bf6e;"></path>';
                                potHTML = potHTML + '            </svg>';
                                potHTML = potHTML + '            <svg id="OptionGoldDown" class="mr10" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 32 20">';
                                potHTML = potHTML + '               <path data-name="Path 3636" d = "m11.6 26-3.664-3.817 7.808-8.133 6.4 6.667L34 8.35 31.744 6l-9.6 10-6.4-6.667-10.08 10.484L2 16v10z" transform = "translate(-2 -6)" style = "fill:#e10000;" ></path >';
                                potHTML = potHTML + '            </svg >';
                                potHTML = potHTML + '            <span>' + Pots[i].symbol + ' <span class="medium OptionNIFTY ' + goldid + '" id="OptionGOLD">0.0000</span></span>';
                            }
                            else {
                                potHTML = potHTML + '            <svg id="" class="mr10" data-name="trending_up_black_24dp (5)" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 69.351 69.351">';
                                potHTML = potHTML + '                <path data-name="Path 3164" d="m42.455 6 6.617 6.617-14.1 14.1-11.56-11.557L2 36.6l4.074 4.074 17.338-17.336L34.971 34.9l18.2-18.176 6.617 6.617V6z" transform="translate(3.779 11.338)" style="fill:#27bf6e"></path>';
                                potHTML = potHTML + '            </svg>';
                                potHTML = potHTML + '            <svg id="" class="mr10" xmlns="http://www.w3.org/2000/svg" width="30" height="30" viewBox="0 0 32 20">';
                                potHTML = potHTML + '               <path data-name="Path 3636" d = "m11.6 26-3.664-3.817 7.808-8.133 6.4 6.667L34 8.35 31.744 6l-9.6 10-6.4-6.667-10.08 10.484L2 16v10z" transform = "translate(-2 -6)" style = "fill:#e10000" ></path >';
                                potHTML = potHTML + '            </svg >';
                                potHTML = potHTML + '            <span>' + Pots[i].symbol + ' <span class="medium ">0.0000</span></span>';
                            }
                            potHTML = potHTML + '        </div>';
                            potHTML = potHTML + '    </div>';
                            potHTML = potHTML + '    <div class="column">';
                            if (Pots[i].symbol == 'USDINR') {
                                potHTML = potHTML + '        <div class=" ' + usdinrid + 'PerChange OptionUSDINRPerChange" id="' + usdinrid + 'PerChange">00.00 (0.00%)</div>';
                            }
                            else if (Pots[i].symbol == 'BANKNIFTY') {
                                potHTML = potHTML + '        <div class=" ' + bankniftyid + 'PerChange" id="' + bankniftyid + 'PerChange">00.00 (0.00%)</div>';
                            }
                            else if (Pots[i].symbol == 'NIFTY') {
                                potHTML = potHTML + '        <div class=" ' + niftyid + 'PerChange" id="' + niftyid + 'PerChange">00.00 (0.00%)</div>';
                            }
                            else if (Pots[i].symbol == 'GOLD') {
                                potHTML = potHTML + '        <div class=" ' + goldid + 'PerChange" id="' + goldid + 'PerChange">00.00 (0.00%)</div>';
                            }
                            else {
                                potHTML = potHTML + '        <div class="greencolor">00.00 (0.00%)</div>';
                            }
                            potHTML = potHTML + '    </div>';
                            potHTML = potHTML + '</div >';
                            potHTML = potHTML + '<div class="mtop10"></div>';
                            potHTML = potHTML + '<div class="card">';
                            potHTML = potHTML + '    <div class="topinner">';
                            potHTML = potHTML + '        <div class="left">';
                            potHTML = potHTML + '            <div class="if">';
                            potHTML = potHTML +                 Pots[i].symbol +' '+Pots[i].description;
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '            <div class="mx">';
                            potHTML = potHTML + '                    Max Profit';
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '            <div class="rupp"><span class="ruppmax">';
                            potHTML = potHTML + '                    ₹' + Math.round(Pots[i].maxProfit).toLocaleString('en-IN')+'';
                            potHTML = potHTML + '            </span></div>';
                            potHTML = potHTML + '        </div>';
                            potHTML = potHTML + '        <div class="right">';
                            potHTML = potHTML + '            <div class="rfunds">';
                            potHTML = potHTML + '                    Required Funds';
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '            <div class="amt"><span class="amtall">';
                            potHTML = potHTML + '             ₹' + Math.round(Pots[i].requiredFunds).toLocaleString('en-IN')+'';
                            potHTML = potHTML + '             </span></div>';
                            potHTML = potHTML + '            <div class="ml">';
                            potHTML = potHTML + '                    Max Loss';
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '            <div class="amtmax"><span class="amtall">';
                            potHTML = potHTML + '             ₹' + Math.round(Pots[i].maxLoss).toLocaleString('en-IN') + '';
                            potHTML = potHTML + '            </span></div>';
                            potHTML = potHTML + '        </div>';
                            potHTML = potHTML + '    </div>';
                            potHTML = potHTML + '   <div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + Pots[i].maxProfit + '</span>';
                            potHTML = potHTML + '        <span class="requiredfundsdefault">' + Pots[i].requiredFunds + '</span>';
                            potHTML = potHTML + '        <span class="maxLossdefault">' + Pots[i].maxLoss + '</span><span class="MegamaxLotSize">' + Pots[i].maxLotSize + '</span><span class="MegalotSize">' + Pots[i].lotSize + '</span><span class="Megasymbol">' + Pots[i].symbol + '</span></div>';
                            potHTML = potHTML + '    <div class="botinner">';
                            potHTML = potHTML + '        <div class="two-block fourty">';
                            potHTML = potHTML + '            <div class="column">';
                            potHTML = potHTML + '                <div class="counterblock white" id="cutinput">';
                            potHTML = potHTML + '                    <div class="input-group">';
                            potHTML = potHTML + '                        <input type="button" class="button-minus" data-field="quantity">';
                            potHTML = potHTML + '                        <div class="holder">';
                            if (Pots[i].symbol == 'USDINR') {
    
                                potHTML = potHTML + '                            <input onchange="updateRates(event)"  type="number" step="1" max="" value="5" name="quantity" class="quantity-field" id="qty_' + Pots[i].id + '"> <span class="ltsize">Lot</span>';
                            }
                            else {
                                potHTML = potHTML + '                            <input onchange="updateRates(event)"  type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + Pots[i].id + '"> <span class="ltsize">Lot</span>';
    
                            }
                            potHTML = potHTML + '                        </div>';
                            potHTML = potHTML + '                        <input type="button" class="button-plus" data-field="quantity">';
                            potHTML = potHTML + '                    </div>';
                            potHTML = potHTML + '                </div>';
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '            <div class="column">';
                            potHTML = potHTML + '                <div class="twoblock no-wrap">';
                            potHTML = potHTML + '                    <div class="column ">';
                            potHTML = potHTML + '                        <a class="cta detail custom openslidedrawwer" onclick="GetStrategyDetails(' + Pots[i].id + ', 2, 1,\'INVESTOR\',\'Mega Free Options Strategies\',\'None\',\'details\',\'' + Pots[i].maxLotSize + '\',event)">Details</a>';
                            potHTML = potHTML + '                    </div>';
                            potHTML = potHTML + '                    <div class="column">';
                            potHTML = potHTML + '                        <a href="#confirmorder" class="cta trades custom" onclick="GetStrategyDetails(' + Pots[i].id + ', 2, 1,\'INVESTOR\',\'Mega Free Options Strategies\',\'None\',\'trade\',\'' + Pots[i].maxLotSize + '\',event)">Trade</a>';
                            potHTML = potHTML + '                    </div>';
                            potHTML = potHTML + '                </div>';
                            potHTML = potHTML + '                <div class="newctablock">';
                            potHTML = potHTML + '                    <div class="details">';
                            potHTML = potHTML + '                    </div>';
                            potHTML = potHTML + '                    <div class="trade">';
                            potHTML = potHTML + '                    </div>';
                            potHTML = potHTML + '                </div>';
                            potHTML = potHTML + '            </div>';
                            potHTML = potHTML + '        </div>';
                            potHTML = potHTML + '    </div>';
                            potHTML = potHTML + '</div>';
                            potHTML = potHTML + '</div>';
                        }
                        $("#MegaPots").html(potHTML);
                        $('#OptionBANKNIFTYDown').hide();
                        $('#OptionNIFTYDown').hide();
                        $('#OptionUSDINRDown').hide();
    
                        $("#bestpot").show();
                        if (typeof isBcastConnected === "undefined" || isBcastConnected == false) {
                            //$("#dvLoader").show();
                            var refreshId = setInterval(function () {
                            if (typeof isBcastConnected !== "undefined" && isBcastConnected == true) {
                                //clearInterval(refreshId);
                                SendToBServer(CreateScripDatabyExchCode('0', '0', "1"));
                                SendToBServer(CreateScripDatabyExchCode('3', '3', "1"));
                                SendToBServer(CreateScripDatabyExchCode('2', '57919', "1"));
                            }
                            }, 1000);
                        }
                        $('input').change();
                    }
                },
                error: function (xhr, textStatus, errorThrown) {
                    val = "";
                }
            });
             $('.input-group').on('click', '.button-plus', function (e) {
                incrementValue(e);
            });
            $('.input-group').on('click', '.button-minus', function (e) {
                decrementValue(e);
            });
    
            function incrementValue(e) {
                //debugger;
                e.preventDefault();
                var fieldName = $(e.target).data('field');
                var parent = $(e.target).closest('div');
                var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
                var MegamaxLotSize = 0,LotSize =0, SYmbol = "";
                if (!isNaN(currentVal)) {
                    MegamaxLotSize = Number($(e.target).closest('.card').children('.hiddendefaultvalues').children('.MegamaxLotSize').html());
                    LotSize = $(e.target).closest('.card').children('.hiddendefaultvalues').children('.MegalotSize').html();
                    SYmbol = $(e.target).closest('.card').children('.hiddendefaultvalues').children('.Megasymbol').html();
                    if (currentVal == 1) {
                        maxprofitbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
                        Reqfundbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.requiredfundsdefault').html());
                        maxlossbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.maxLossdefault').html());
    
                        //maxprofitbasevalue = removeSeparator($(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html());
                        //Reqfundbasevalue = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html());
                        //maxlossbasevalue = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html());
                        //maxprofitbasevalue = maxprofitbasevalue.replace(/₹/g, "")
                        //Reqfundbasevalue = Reqfundbasevalue.replace(/₹/g, "")
                        //maxlossbasevalue = maxlossbasevalue.replace(/₹/g, "")
                    }
                    parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
                    var Getmaxprofit = 0;
                    var RequiredFund = 0;
                    var Maxloss = 0;
                    var Onlyupdatelen = 0
                    Onlyupdatelen = currentVal + 1
                    //if (Onlyupdatelen > 0) {
                    //    for (let i = 0; i < Onlyupdatelen; i++) {
                    //        Getmaxprofit = parseInt(Getmaxprofit) + parseInt(maxprofitbasevalue)
                    //        RequiredFund = parseInt(RequiredFund) + parseInt(Reqfundbasevalue)
                    //        Maxloss = parseInt(Maxloss) + parseInt(maxlossbasevalue)
                    //    }
                    //}
                    maxprofitbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
                    Reqfundbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.requiredfundsdefault').html());
                    maxlossbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.maxLossdefault').html());
                    //if (SYmbol == "USDINR") {
                    //    MegamaxLotSize = (MegamaxLotSize / LotSize);
                    //}
                    //else {
                    //    MegamaxLotSize = MegamaxLotSize;
                    //}
                    if (Onlyupdatelen >= MegamaxLotSize) {
                        Onlyupdatelen = MegamaxLotSize
                        currentVal = MegamaxLotSize
                        parent.find('input[name=' + fieldName + ']').val(currentVal);
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-plus').css('opacity', '0.3');
                    }
                    else {
                        parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
                    }
    
                    Getmaxprofit = Onlyupdatelen * maxprofitbasevalue;
                    RequiredFund = Onlyupdatelen * Reqfundbasevalue;
                    Maxloss = Onlyupdatelen * maxlossbasevalue;
    
                    Getmaxprofit = Math.round(Getmaxprofit).toLocaleString('en-IN');
                    RequiredFund = Math.round(RequiredFund).toLocaleString('en-IN');
                    Maxloss = Math.round(Maxloss).toLocaleString('en-IN');
                    $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Getmaxprofit);
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + RequiredFund);
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Maxloss);
                    if (Onlyupdatelen > 1) {
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '1');
                    }
                   // }
                    //else {
                    //    //alert("Lot Can't be greater than Max Lot Size of MegamaxLotSize" + MegamaxLotSize);
                    //    //return;
                    //}
                }
                else {
                    parent.find('input[name=' + fieldName + ']').val(0);
                }
            }
            function decrementValue(e) {
                e.preventDefault();
                var fieldName = $(e.target).data('field');
                var parent = $(e.target).closest('div');
                var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
                if (!isNaN(currentVal) && currentVal > 1) {
                    maxprofitbasevalueless = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
                    Reqfundbasevalueless = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.requiredfundsdefault').html());
                    maxlossbasevalueless = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.maxLossdefault').html());
                    $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-plus').css('opacity', '1');
                    //maxprofitbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html());
                    //Reqfundbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html());
                    //maxlossbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html());
                    //maxprofitbasevalueless = maxprofitbasevalueless.replace(/₹/g, "")
                    //Reqfundbasevalueless = Reqfundbasevalueless.replace(/₹/g, "")
                    //maxlossbasevalueless = maxlossbasevalueless.replace(/₹/g, "")
                    //maxprofitbasevalueless = (maxprofitbasevalueless / currentVal)
                    //Reqfundbasevalueless = (Reqfundbasevalueless / currentVal)
                    //maxlossbasevalueless = (maxlossbasevalueless / currentVal)
                    parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
                    var Getmaxprofitless = 0;
                    var RequiredFundless = 0;
                    var Maxlossless = 0;
                    var Onlyupdatelenless = 0
                    Onlyupdatelenless = currentVal - 1
                    if (Onlyupdatelenless > 0) {
                        //for (let i = 0; i < Onlyupdatelenless; i++) {
                        //    Getmaxprofitless = parseInt(Getmaxprofitless) + parseInt(maxprofitbasevalueless)
                        //    RequiredFundless = parseInt(RequiredFundless) + parseInt(Reqfundbasevalueless)
                        //    Maxlossless = parseInt(Maxlossless) + parseInt(maxlossbasevalueless)
                        //}
    
                        Getmaxprofitless = Onlyupdatelenless * maxprofitbasevalueless;
                        RequiredFundless = Onlyupdatelenless * Reqfundbasevalueless;
                        Maxlossless = Onlyupdatelenless * maxlossbasevalueless;
    
                        Getmaxprofitless = Math.round(Getmaxprofitless).toLocaleString('en-IN');
                        RequiredFundless = Math.round(RequiredFundless).toLocaleString('en-IN');
                        Maxlossless = Math.round(Maxlossless).toLocaleString('en-IN');
    
                        $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Getmaxprofitless);
                        $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + RequiredFundless);
                        $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Maxlossless);
                    }
                    else {
                        $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + maxprofitbasevalue);
                        $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Reqfundbasevalue);
                        $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + maxlossbasevalue);
                    }
                    if (Onlyupdatelenless == 1) {
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '0.3');
                    }
                }
                else {
                    parent.find('input[name=' + fieldName + ']').val(1);
                    {
                        maxprofitbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html());
                        maxlossbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html());
                        Reqfundbasevalueless = removeSeparator($(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html());
                    }
                }
            }
            /****plus minus input****/
        });
        function updateRatesOther(e) {
            debugger;
            var maxprofitotherbasevalue = 0, Reqfundotherbasevalue = 0, maxLotSizeOther = 0, Symbol = "", LotSize = 0;
                maxprofitotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
                Reqfundotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.requiredfundsotherdefault').html());
            maxLotSizeOther = Number($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.maxLotSizeOther').html());
            Symbol = $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.symbolOther').html();
            LotSize = $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.lotSizeOther').html();
                if (e.target.value != '' && e.target.value != '0' && parseInt((e.target.value), 10) != 0) {
                    var currentVal = parseInt((e.target.value), 10);
                    if (!isNaN(currentVal)) {
                    //if (Symbol == "USDINR") {
                    //    maxLotSizeOther = maxLotSizeOther / LotSize;
                    //}
                    //else {
                    //    maxLotSizeOther = maxLotSizeOther;
                    //}
                    if (currentVal >= Number(maxLotSizeOther)) {
                        currentVal = maxLotSizeOther
                        e.target.value = maxLotSizeOther;
                        $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-plusother').css('opacity', '0.3');
                    }
                    else {
                        $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-plusother').css('opacity', '1');
                    }
                        var Getmaxprofitother = maxprofitotherbasevalue * currentVal;
                        var RequiredFundother = Reqfundotherbasevalue * currentVal;
                        $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Math.round(Getmaxprofitother).toLocaleString('en-IN'));
                        $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + Math.round(RequiredFundother).toLocaleString('en-IN'));
                        if (currentVal > 1) {
                            $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '1');
                        } else {
                            $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '0.3');
                        }
                   // }
                    //else {
                    //    /*alert("Lot Can't be greater than Max Lot Size of " + maxLotSizeOther);*/
                    //    e.target.value = 1;
                    //    var Getmaxprofitother = maxprofitotherbasevalue * 1;
                    //    var RequiredFundother = Reqfundotherbasevalue * 1;
                    //    e.target.value = 1;
                    //    var Getmaxprofitother = maxprofitotherbasevalue * 1;
                    //    var RequiredFundother = Reqfundotherbasevalue * 1;
                    //    $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '0.3');
                    //    $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Math.round(Getmaxprofitother).toLocaleString('en-IN'));
                    //    $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + Math.round(RequiredFundother).toLocaleString('en-IN'));
                    //}
                    }
                    else {
                        e.target.value = 1;
                        var Getmaxprofitother = maxprofitotherbasevalue * 1;
                        var RequiredFundother = Reqfundotherbasevalue * 1;
                        $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '0.3');
                        $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Math.round(Getmaxprofitother).toLocaleString('en-IN'));
                        $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + Math.round(RequiredFundother).toLocaleString('en-IN'));
                    }
                }
                else {
                    e.target.value = 1;
                    var Getmaxprofitother = maxprofitotherbasevalue * 1;
                    var RequiredFundother = Reqfundotherbasevalue * 1;
                    $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '0.3');
                    $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Math.round(Getmaxprofitother).toLocaleString('en-IN'));
                    $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + Math.round(RequiredFundother).toLocaleString('en-IN'));
                    $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '0.3');
                }
        }
        function updateRates(e) {
            debugger;
            var maxprofitbasevalue = 0, Reqfundbasevalue = 0, maxlossbasevalue = 0, MegamaxLotSize = 0, LotSize = 0, SYmbol = "";
            maxprofitbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
            Reqfundbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.requiredfundsdefault').html());
            maxlossbasevalue = removeSeparator($(e.target).closest('.card').children('.hiddendefaultvalues').children('.maxLossdefault').html());
            MegamaxLotSize = Number($(e.target).closest('.card').children('.hiddendefaultvalues').children('.MegamaxLotSize').html());
            LotSize = $(e.target).closest('.card').children('.hiddendefaultvalues').children('.MegalotSize').html();
            SYmbol = $(e.target).closest('.card').children('.hiddendefaultvalues').children('.Megasymbol').html();
            if (e.target.value != '' && e.target.value != '0' && parseInt((e.target.value), 10) != 0) {
                var currentVal = parseInt((e.target.value), 10);
                if (!isNaN(currentVal)) {
                    //if (SYmbol == "USDINR") {
                    //    MegamaxLotSize = (MegamaxLotSize / LotSize);
                    //}
                    //else {
                    //    MegamaxLotSize = MegamaxLotSize;
                    //}
                    if (currentVal >= MegamaxLotSize) {
                        currentVal = MegamaxLotSize
                        e.target.value = MegamaxLotSize;
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-plus').css('opacity', '0.3');
                    }
                    else {
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-plus').css('opacity', '1');
                    }
                    var MaxProfit = maxprofitbasevalue * currentVal;
                    var RequiredFund = Reqfundbasevalue * currentVal;
                    var MaxLoss = maxlossbasevalue * currentVal;
                    $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Math.round(MaxProfit).toLocaleString('en-IN'));
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Math.round(RequiredFund).toLocaleString('en-IN'));
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Math.round(MaxLoss).toLocaleString('en-IN'));
                     if (currentVal > 1) {
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '1');
                    } else {
                        $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '0.3');
                    }
                    //}
                    //else {
                    //    /*alert("Lot Can't be greater than Max Lot Size of " + MegamaxLotSize);*/
                    //    e.target.value = 1;
                    //    var MaxProfit = maxprofitbasevalue * 1;
                    //    var RequiredFund = Reqfundbasevalue * 1;
                    //    var MaxLoss = Reqfundbasevalue * 1;
                    //    (e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Math.round(MaxProfit).toLocaleString('en-IN'));
                    //    $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Math.round(RequiredFund).toLocaleString('en-IN'));
                    //    $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Math.round(MaxLoss).toLocaleString('en-IN'));
                    //    return;
                    //}
                }
                else {
                    e.target.value = 1;
                    var MaxProfit = maxprofitbasevalue * 1;
                    var RequiredFund = Reqfundbasevalue * 1;
                    var MaxLoss = Reqfundbasevalue * 1;
                    $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Math.round(MaxProfit).toLocaleString('en-IN'));
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Math.round(RequiredFund).toLocaleString('en-IN'));
                    $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Math.round(MaxLoss).toLocaleString('en-IN'));
                    $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '0.3');
                    }
            }
            else {
                e.target.value = 1;
                var MaxProfit = maxprofitbasevalue * 1;
                var RequiredFund = Reqfundbasevalue * 1;
                var MaxLoss = Reqfundbasevalue * 1;
                $(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + Math.round(MaxProfit).toLocaleString('en-IN'));
                $(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Math.round(RequiredFund).toLocaleString('en-IN'));
                $(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + Math.round(MaxLoss).toLocaleString('en-IN'));
                $(e.target).closest('.card').children('.botinner').children('.two-block').children('.column').children('.counterblock').children('.input-group').children('.button-minus').css('opacity', '0.3');
            }
        }
        function incrementValuother(e) {
            e.preventDefault();
            var fieldName = $(e.target).data('field');
            var parent = $(e.target).closest('div');
            var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
            var maxprofitotherbasevalue = 0, Reqfundotherbasevalue = 0, maxLotSizeOther = 0, Symbol = "", LotSize = 0 ;
            maxprofitotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
            Reqfundotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.requiredfundsotherdefault').html());
            maxLotSizeOther = Number($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.maxLotSizeOther').html());
            Symbol = $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.symbolOther').html();
            LotSize = $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.lotSizeOther').html();
    
           // maxprofitotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
           // Reqfundotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.requiredfundsotherdefault').html());
            if (!isNaN(currentVal)) {
                if (currentVal == 1) {
                    maxprofitotherbasevalue = maxprofitotherbasevalue.replace(/₹/g, "")
                    Reqfundotherbasevalue = Reqfundotherbasevalue.replace(/₹/g, "")
                }
                if (currentVal == 0) {
                    parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
                    return false;
                }
                parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
                var Getmaxprofitother = 0;
                var RequiredFundother = 0;
                var Onlyupdatelen = 0
                Onlyupdatelen = currentVal + 1
                //if (Symbol == "USDINR") {
                //    maxLotSizeOther = maxLotSizeOther / LotSize;
                //}
                //else {
                //    maxLotSizeOther = maxLotSizeOther;
                //}
                if (Onlyupdatelen >= number(maxLotSizeOther)) {
                    Onlyupdatelen = maxLotSizeOther
                    currentVal = maxLotSizeOther
                    parent.find('input[name=' + fieldName + ']').val(currentVal);
                    $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-plusother').css('opacity', '0.3');
                }
                else {
                    parent.find('input[name=' + fieldName + ']').val(currentVal + 1);
                }
                if (Onlyupdatelen > 0) {
                    //for (let i = 0; i < Onlyupdatelen; i++) {
                    //    Getmaxprofitother = parseInt(Getmaxprofitother) + parseInt(maxprofitotherbasevalue)
                    //    RequiredFundother = parseInt(RequiredFundother) + parseInt(Reqfundotherbasevalue)
                    //}
    
                    var Getmaxprofitother = maxprofitotherbasevalue * Onlyupdatelen;
                    var RequiredFundother = Reqfundotherbasevalue * Onlyupdatelen;
                }
                else {
                    $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + maxprofitotherbasevalue);
                    $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + Reqfundotherbasevalue);
                }
                Getmaxprofitother = Math.round(Getmaxprofitother).toLocaleString('en-IN');
                RequiredFundother = Math.round(RequiredFundother).toLocaleString('en-IN');
                $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Getmaxprofitother);
                $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + RequiredFundother);
                if (Onlyupdatelen > 1) {
                    $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity', '1');
                }
                //}
                //else {
                //    //alert("Lot Can't be greater than Max Lot Size of " + Onlyupdatelen + maxLotSizeOther);
                //    //return;
                //}
            }
            else {
                parent.find('input[name=' + fieldName + ']').val(0);
            }
        }
        function decrementValueother(e) {
            e.preventDefault();
            var fieldName = $(e.target).data('field');
            var parent = $(e.target).closest('div');
            var currentVal = parseInt(parent.find('input[name=' + fieldName + ']').val(), 10);
            var maxprofitotherbasevalueless = 0, Reqfundotherbasevalueless = 0;
            maxprofitotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
            Reqfundotherbasevalue = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.requiredfundsotherdefault').html());
            $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-plusother').css('opacity', '1');
            //maxprofitotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.ruppeeMaxprofitdefault').html());
            //Reqfundotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.hiddendefaultvalues').children('.requiredfundsotherdefault').html());
            if (!isNaN(currentVal) && currentVal > 1) {
                maxprofitotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html());
                Reqfundotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html());
                maxprofitotherbasevalueless = maxprofitotherbasevalueless.replace(/₹/g, "")
                Reqfundotherbasevalueless = Reqfundotherbasevalueless.replace(/₹/g, "")
                maxprofitotherbasevalueless = (maxprofitotherbasevalueless / currentVal)
                Reqfundotherbasevalueless = (Reqfundotherbasevalueless / currentVal)
                parent.find('input[name=' + fieldName + ']').val(currentVal - 1);
                var Getmaxprofitotherless = 0;
                var RequiredFundotherless = 0;
                var Onlyupdatelenless = 0
    
                Onlyupdatelenless = currentVal - 1
    
                if (Onlyupdatelenless > 0) {
    
    
    
                    //for (let i = 0; i < Onlyupdatelenless; i++) {
    
                    //    Getmaxprofitotherless = parseInt(Getmaxprofitotherless) + parseInt(maxprofitotherbasevalueless)
                    //    RequiredFundotherless = parseInt(RequiredFundotherless) + parseInt(Reqfundotherbasevalueless)
    
                    //}
    
                    var Getmaxprofitotherless = maxprofitotherbasevalueless * Onlyupdatelenless;
                    var RequiredFundotherless = Reqfundotherbasevalueless * Onlyupdatelenless;
    
                    Getmaxprofitotherless = Math.round(Getmaxprofitotherless).toLocaleString('en-IN');
                    RequiredFundotherless = Math.round(RequiredFundotherless).toLocaleString('en-IN');
    
    
                    $(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html('₹' + Getmaxprofitotherless);
                    $(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html('₹' + RequiredFundotherless);
    
                    if (Onlyupdatelenless == 1) {
                        $(e.target).closest('.greybox').children('.innerwhite').children('.twoblockcust').children('.column').children('.counterblock').children('.input-group').children('.button-minusother').css('opacity','0.3');
                    }
                }
                else {
                    return false;
    
                    //$(e.target).closest('.card').children('.topinner').children('.left').children('.rupp').children('.ruppmax').html('₹' + maxprofitbasevalueless);
                    //$(e.target).closest('.card').children('.topinner').children('.right').children('.amt').children('.amtall').html('₹' + Reqfundbasevalueless);
                    //$(e.target).closest('.card').children('.topinner').children('.right').children('.amtmax').children('.amtall').html('₹' + maxlossbasevalueless);
    
                }
    
            }
            else {
                parent.find('input[name=' + fieldName + ']').val(1);
                {
    
                    //maxprofitotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innergrey').children('.tpsection').children('.left').children('.ruppee').children('.ruppeeMaxprofit').html());
                    //Reqfundotherbasevalueless = removeSeparator($(e.target).closest('.greybox').children('.innerwhite').children('.requiredfunds').children('.requiredfundsother').html());
    
                }
            }
    
    
        }
    
            $('.customswitch input').click(function () {
                $('.customswitch .option').removeClass("active")
                $(this).parent().addClass("active");
            });
    
    
            $('.cta.confirm').click(function () {
                $('#strategiesslide').removeClass("open");
                $('body').removeClass("act")
            });
    
            $('.promolabel svg').click(function () {
                $('body').toggleClass("openpromode");
                $('.tooltipbox').fadeIn();
    
            });
            $('.backdrop').click(function () {
                $('body').removeClass("openpromode")
                $('.tooltipbox').fadeOut();
            });
            $('.viewalloptions').click(function(){
                $('body').addClass("act")
                $('#viewallstrategies').addClass("open")
            });
            $('.topheadr svg').click(function(){
                $('#viewallstrategies').removeClass("open");
                $('body').removeClass("act")
            });
            $('.openfreeslide').click(function(){
                $('body').addClass("act");
                $('#strategiesslide.free').addClass("open");
                $('#viewallstrategies').removeClass("open")
            });
    
            $('#strategiesslide.free .close').click(function () {
                $('#strategiesslide.free').removeClass("open");
                $('body').removeClass("act")
            });
    
    
    
            $('.openslidedrawwer').click(function () {
                $('body').addClass("act")
                $('#strategiesslide.paid').addClass("open")
            });
            $('#strategies .free .innerscroll .top .close').click(function () {
    
                $("#strategiesslide").removeClass("open");
                $('body').removeClass("act")
            });
        //$('.close').click(function () {
    
        //    $("#strategiesslide").removeClass("open");
        //    $('body').removeClass("act")
        //});
            $('#strategiesslide.paid .close').click(function () {
                $('#strategiesslide.paid').removeClass("open");
                $('body').removeClass("act")
            });
            $('.confirmorder').click(function(){
                $('#strategiesslide.paid').removeClass("open");
            });
    
            /*************bottom Sheets******************/
            $('.activate.cta').click(function(){
                $('body').addClass("activateoptions");
            });
            $('.cta.trade').click(function(){
                $('body').addClass("confirmorder");
            });
            $('.cta.confirm.confirmorder').click(function(){
                $('body').addClass("orderplaced");
            });
    
    
    
    
        //SendToBServer(CreateScripDatabyExchCode(2, 62808, "1"));
    
        function ajaxCall(type, action, param, async) {
            var ajaxResult;
            $.support.cors = true;
            url = action;
            $.ajax(
                {
                    type: type,
                    dataType: 'JSON',
                    crossDomain: true,
                    url: url,
                    data: param,
                    async: async,
                    success: function (response) {
                        ajaxResult = response;
                    },
                    error: function (err) {
                        ajaxResult = undefined;
                    }
                });
            return ajaxResult;
        }
    
        function DashboardSTARTER(displayCount) {
            //debugger;
            $("#one-tab").hide();
            $("#two-tab").hide();
            $("#three-tab").hide();
            $("#four-tab").hide();
            $("#five-tab").hide();
    
    
            $("#btnViewMore").hide();
            //btnViewMore
            var para = {
                PottypeName: "FreePot",
                predictionTypeName: "NA",
                ConditionID: Starterid,
                Conditioname: Startercondition,
            };
            var res = ajaxCall('POST', '/Home/GetOptionstoreConditions', para, false);
           // console.clear();
            console.log(res.data.filters)
            $("#OtherFreeOptionsStrategies").empty();
            if (res.data != null) {
                if (res.data.filters != null) {
                    for (var i = 0; i < res.data.filters.length; i++) {
                        switch (res.data.filters[i].id) {
                            case "Starter":
                                Starterid = res.data.filters[i].id;
                                Startercondition = res.data.filters[i].condition;
                                $("#one-tab").html(res.data.filters[i].label);
                                $("#one-tab").show();
                                break;
                            case "Margin10K":
                                Margin10Kid = res.data.filters[i].id;
                                Margin10Kidcondition = res.data.filters[i].condition;
                                $("#two-tab").html(res.data.filters[i].label);
                                $("#two-tab").show();
                                break;
                            case "MaxLoss2K":
                                MaxLossId = res.data.filters[i].id;
                                MaxLossIdcondition = res.data.filters[i].condition;
                                $("#three-tab").html(res.data.filters[i].label);
                                $("#three-tab").show();
                                break;
                            case "Strategy":
                                StrategyMultileg = res.data.filters[i].id;
                                StrategyMultilegcondition = res.data.filters[i].condition;
                                $("#four-tab").html(res.data.filters[i].label);
                                $("#four-tab").show();
                                break;
                            case "OnlySell":
                                OnlySellID = res.data.filters[i].id;
                                OnlySellcondition = res.data.filters[i].condition;
                                $("#five-tab").html(res.data.filters[i].label);
                                $("#five-tab").show();
                                break;
                            default: break;
                        }
                    }
    
                }
            }
            if (res.data != null && res.data.pots != null && res.data.pots.length > 0) {
                var STARTERView = '';
                var STARTERViewRow = '';
                STARTERView = res.data.pots;
                console.log(STARTERView)
                var STARTERlen = STARTERView.length;
                if (STARTERlen > 0) {
                    if (STARTERlen < displayCount) {
    
                        displayCount = STARTERlen;
                    }
    
                    for (let i = 0; i < displayCount; i++) {
                        {
                            STARTERView[i].maxProfit = Math.round(STARTERView[i].maxProfit);
                            STARTERView[i].requiredFunds = Math.round(STARTERView[i].requiredFunds);
                            var Recommendstatus = ''
                            var isRecommended = STARTERView[i].isRecommended;
                            if (isRecommended == false) {
    
                                Recommendstatus = '';
                            }
                            else {
                                Recommendstatus = 'RECOMMENDED';
                            }
    
                            STARTERViewRow += '<div class="greybox ">'
                                + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + STARTERView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'details\',event)">'
                                + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                + '<span class="ruppeeMaxprofit" >₹' + Math.round(STARTERView[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                    + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + STARTERView[i].maxProfit + '</span>'
                                        + '<span class="requiredfundsotherdefault">' + STARTERView[i].requiredFunds + '</span></div > '
                                + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                + '<div class="pairname" id="othrFreOptdesc"><b>' + STARTERView[i].symbol + '</b>' + '&nbsp;' + STARTERView[i].description + '</div></div>'
                                + '<div class="innerwhite">';
                            if (isRecommended) {
                                STARTERViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                            }
                            STARTERViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                + '<span class="requiredfundsother">₹ ' + Math.round(STARTERView[i].requiredFunds).toLocaleString('en-IN')+ '</span></div > '
                                + '<div class="twoblockcust mtop5"><div class="column">'
                                + '<div class="counterblock white other " id="cutinput">'
                                + '<div class="input-group">'
                                + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                + '<div class="holder">'
                                + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + STARTERView[i].id + '"> <span class="ltsize">Lot</span></div>'
                                + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + STARTERView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'trade\',event)">Trade</a></div></div></div>';
    
                            if (STARTERView[i].tradeCount > 0) {
                                STARTERViewRow += '<div class="tradedvalue">'
                                    + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                    + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                    + '<path data-name="Path 8"'
                                    + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                    + 'style="fill:#ff881c" ></path></svg>';
                                STARTERViewRow += '<small>' + STARTERView[i].tradeCount + ' user traded</small></div>';
                            }
                            STARTERViewRow += '</div>';
    
                            $("#OtherFreeOptionsStrategies").html(STARTERViewRow);
    
                        }
                    }
                    if (STARTERlen > 3) {
                        $("#btnViewMore").show();
                        $("#btnViewMore").click(function () { DashboardSTARTER(STARTERlen) });
    
                    }
                }
            }
            else {
                DashboardREQFundless10K(3);
                $("#one-tab").hide();
                $("#two").attr('checked', true);
            }
    
        }
        function DashboardREQFundless10K(displayCount) {
            $("#btnViewMore").hide();
    
            var para = {
                PottypeName: "FreePot",
                predictionTypeName: "NA",
                ConditionID: Margin10Kid,
                Conditioname: Margin10Kidcondition,
            };
    
            $("#OtherFreeOptionsStrategiespaneltwo").empty();
            var res = ajaxCall('POST', '/Home/GetOptionstoreConditions', para, false);
    
            if (res.data != null) {
                var REQFundless10KView = '';
                var REQFundless10KViewrow = '';
                REQFundless10KView = res.data.pots;
                var REQFundless10KViewlen = REQFundless10KView.length;
                if (REQFundless10KViewlen > 0) {
                    if (REQFundless10KViewlen < displayCount) {
    
                        displayCount=REQFundless10KViewlen;
                    }
    
                    for (let i = 0; i < displayCount; i++) {
                        {
    
                            REQFundless10KView[i].maxProfit = Math.round(REQFundless10KView[i].maxProfit);
                            REQFundless10KView[i].requiredFunds = Math.round(REQFundless10KView[i].requiredFunds);
                            var Recommendstatus = ''
                            var isRecommended = REQFundless10KView[i].isRecommended;
                            if (isRecommended == false) {
    
                                Recommendstatus = '';
                            }
                            else {
                                Recommendstatus = 'RECOMMENDED';
                            }
    
                            REQFundless10KViewrow += '<div class="greybox ">'
                                + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + REQFundless10KView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'details\',event)">'
                                + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                + '<span class="ruppeeMaxprofit" >₹' + Math.round(REQFundless10KView[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + REQFundless10KView[i].maxProfit + '</span>'
                                + '<span class="requiredfundsotherdefault">' + REQFundless10KView[i].requiredFunds + '</span></div > '
                                + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                + '<div class="pairname" id="othrFreOptdesc"><b>' + REQFundless10KView[i].symbol + '</b>' + '&nbsp;' + REQFundless10KView[i].description + '</div></div>'
                                + '<div class="innerwhite">';
                            if (isRecommended) {
                                REQFundless10KViewrow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                            }
                            REQFundless10KViewrow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                + '<span class="requiredfundsother">₹ ' + Math.round(REQFundless10KView[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                + '<div class="twoblockcust mtop5"><div class="column">'
                                + '<div class="counterblock white other " id="cutinput">'
                                + '<div class="input-group">'
                                + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                + '<div class="holder">'
                                + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + REQFundless10KView[i].id + '"> <span class="ltsize">Lot</span></div>'
                                + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + REQFundless10KView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'trade\',event)">Trade</a></div></div></div>';
    
                            if (REQFundless10KView[i].tradeCount > 0) {
                                REQFundless10KViewrow += '<div class="tradedvalue">'
                                    + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                    + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                    + '<path data-name="Path 8"'
                                    + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                    + 'style="fill:#ff881c" ></path></svg>';
                                REQFundless10KViewrow += '<small>' + REQFundless10KView[i].tradeCount + ' user traded</small></div>';
                            }
                            REQFundless10KViewrow += '</div>';
    
                            $("#OtherFreeOptionsStrategiespaneltwo").html(REQFundless10KViewrow);
    
                        }
                    }
                    if (REQFundless10KViewlen > 3) {
                        $("#btnViewMore").show();
                        $("#btnViewMore").click(function () { DashboardREQFundless10K(REQFundless10KViewlen) });
    
                    }
                }
            }
            else {
                DashboardMAXLOSS2K(3);
                $("#two-tab").hide();
                $("#three").attr('checked', true);
            }
    
        }
        function DashboardMAXLOSS2K(displayCount) {
            $("#btnViewMore").hide();
            var para = {
                PottypeName: "FreePot",
                predictionTypeName: "NA",
                ConditionID: MaxLossId,
                Conditioname: MaxLossIdcondition,
            };
            $("#OtherFreeOptionsStrategiespanelthree").html("");
    
            var res = ajaxCall('POST', '/Home/GetOptionstoreConditions', para, false);
    
            if (res.data != null) {
                var MAXLOSS2KView = '';
                var MAXLOSS2KViewRow = '';
                MAXLOSS2KView = res.data.pots;
                var MAXLOSS2Klen = MAXLOSS2KView.length;
                if (MAXLOSS2Klen > 0) {
    
                    if (MAXLOSS2Klen < displayCount) {
    
                        displayCount=MAXLOSS2Klen;
                    }
    
                    for (let i = 0; i < displayCount; i++) {
    
                        MAXLOSS2KView[i].maxProfit = Math.round(MAXLOSS2KView[i].maxProfit);
                        MAXLOSS2KView[i].requiredFunds = Math.round(MAXLOSS2KView[i].requiredFunds);
                        var Recommendstatus = ''
                        var isRecommended = MAXLOSS2KView[i].isRecommended;
                        if (isRecommended == false) {
    
                            Recommendstatus = '';
                        }
                        else {
                            Recommendstatus = 'RECOMMENDED';
                        }
    
                        MAXLOSS2KViewRow += '<div class="greybox ">'
                            + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + MAXLOSS2KView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'details\',event)">'
                            + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                            + '<div class="ruppee" id="othrFreOptMaxProfit">'
                            + '<span class="ruppeeMaxprofit" >₹' + Math.round(MAXLOSS2KView[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + MAXLOSS2KView[i].maxProfit + '</span>'
                                    + '<span class="requiredfundsotherdefault">' + MAXLOSS2KView[i].requiredFunds + '</span></div > '
                            + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                            + '<div class="pairname" id="othrFreOptdesc"><b>' + MAXLOSS2KView[i].symbol + '</b>' + '&nbsp;' + MAXLOSS2KView[i].description + '</div></div>'
                            + '<div class="innerwhite">';
                        if (isRecommended) {
                            MAXLOSS2KViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                        }
                        MAXLOSS2KViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                            + '<span class="requiredfundsother">₹ ' + Math.round(MAXLOSS2KView[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                            + '<div class="twoblockcust mtop5"><div class="column">'
                            + '<div class="counterblock white other " id="cutinput">'
                            + '<div class="input-group">'
                            + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                            + '<div class="holder">'
                            + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + MAXLOSS2KView[i].id + '" > <span class="ltsize">Lot</span></div>'
                            + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                            + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + MAXLOSS2KView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'trade\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                        if (MAXLOSS2KView[i].tradeCount > 0) {
                            MAXLOSS2KViewRow += '<div class="tradedvalue">'
                                + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                + '<path data-name="Path 8"'
                                + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                + 'style="fill:#ff881c" ></path></svg>';
                            MAXLOSS2KViewRow += '<small>' + MAXLOSS2KView[i].tradeCount + ' user traded</small></div>';
                        }
                        MAXLOSS2KViewRow += '</div>';
    
                        $("#OtherFreeOptionsStrategiespanelthree").html(MAXLOSS2KViewRow);
    
                    }
                    if (MAXLOSS2Klen > 3) {
                        $("#btnViewMore").show();
                        $("#btnViewMore").click(function () { DashboardMAXLOSS2K(MAXLOSS2Klen) });
    
                    }
    
                }
            }
    
            else {
                DashboardMultileg(3);
                $("#three-tab").hide();
                $("#four").attr('checked', true);
            }
    
        }
        function DashboardMultileg(displayCount) {
            $("#btnViewMore").hide();
            var para = {
                PottypeName: "FreePot",
                predictionTypeName: "NA",
                ConditionID: StrategyMultileg,
                Conditioname: StrategyMultilegcondition,
            };
    
            $("#OtherFreeOptionsStrategiespanelfour").html("");
    
            var res = ajaxCall('POST', '/Home/GetOptionstoreConditions', para, false);
    
            if (res.data != null) {
                var MultilegView = '';
                var MultilegViewRow = '';
                MultilegView = res.data.pots;
                var MultilegViewlen = MultilegView.length;
                if (MultilegViewlen > 0) {
                    if (MultilegViewlen < displayCount) {
    
                        displayCount = MultilegViewlen;
                    }
    
                    for (let i = 0; i < displayCount; i++) {
    
                        MultilegView[i].maxProfit = Math.round(MultilegView[i].maxProfit);
                        MultilegView[i].requiredFunds = Math.round(MultilegView[i].requiredFunds);
                        var Recommendstatus = ''
                        var isRecommended = MultilegView[i].isRecommended;
                        if (isRecommended == false) {
    
                            Recommendstatus = '';
                        }
                        else {
                            Recommendstatus = 'RECOMMENDED';
                        }
    
                        MultilegViewRow += '<div class="greybox ">'
                            + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + MultilegView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'details\',event)">'
                            + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                            + '<div class="ruppee" id="othrFreOptMaxProfit">'
                            + '<span class="ruppeeMaxprofit" >₹' + Math.round(MultilegView[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + MultilegView[i].maxProfit + '</span>'
                                    + '<span class="requiredfundsotherdefault">' + MultilegView[i].requiredFunds + '</span></div > '
                            + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                            + '<div class="pairname" id="othrFreOptdesc"><b>' + MultilegView[i].symbol + '</b>' + '&nbsp;' + MultilegView[i].description + '</div></div>'
                            + '<div class="innerwhite">';
                        if (isRecommended) {
                            MultilegViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                        }
                        MultilegViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                            + '<span class="requiredfundsother">₹ ' + Math.round(MultilegView[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                            + '<div class="twoblockcust mtop5"><div class="column">'
                            + '<div class="counterblock white other " id="cutinput">'
                            + '<div class="input-group">'
                            + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                            + '<div class="holder">'
                            + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + MultilegView[i].id + '" > <span class="ltsize">Lot</span></div>'
                            + '<input type = "button" class="button-plusother" data-field="quantity" onclick="incrementValuother(event)" ></div></div></div>'
                            + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + MultilegView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'trade\',event)"  class="cta trades custom">Trade</a></div></div></div>';
    
                        if (MultilegView[i].tradeCount > 0) {
                            MultilegViewRow += '<div class="tradedvalue">'
                                + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                + '<path data-name="Path 8"'
                                + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                + 'style="fill:#ff881c" ></path></svg>';
                            MultilegViewRow += '<small>' + MultilegView[i].tradeCount + ' user traded</small></div>';
                        }
                        MultilegViewRow += '</div>';
    
                        $("#OtherFreeOptionsStrategiespanelfour").html(MultilegViewRow);
    
                    }
                    if (MultilegViewlen > 3) {
                        $("#btnViewMore").show();
                        $("#btnViewMore").click(function () { DashboardMultileg(MultilegViewlen) });
    
                    }
                }
            }
            else {
                DashboardOnlySell(3);
                $("#four-tab").hide();
                $("#five").attr('checked', true);
            }
    
        }
        function DashboardOnlySell(displayCount) {
            $("#btnViewMore").hide();
            var para = {
                PottypeName: "FreePot",
                predictionTypeName: "NA",
                ConditionID: OnlySellID,
                Conditioname: OnlySellcondition,
            };
            $("#OtherFreeOptionsStrategiespanelfive").html("");
    
            var res = ajaxCall('POST', '/Home/GetOptionstoreConditions', para, false);
    
            if (res.data != null) {
                var OnlySellView = '';
                var OnlySellViewRow = '';
                OnlySellView = res.data.pots;
                var OnlySellViewlen = OnlySellView.length;
                if (OnlySellViewlen > 0) {
                    if (OnlySellViewlen < displayCount) {
                        displayCount = OnlySellViewlen;
                    }
    
                    for (let i = 0; i < displayCount; i++) {
    
                        OnlySellView[i].maxProfit = Math.round(OnlySellView[i].maxProfit);
                        OnlySellView[i].requiredFunds = Math.round(OnlySellView[i].requiredFunds);
                        var Recommendstatus = ''
                        var isRecommended = OnlySellView[i].isRecommended;
                        if (isRecommended == false) {
    
                            Recommendstatus = '';
                        }
                        else {
                            Recommendstatus = 'RECOMMENDED';
                        }
    
                        OnlySellViewRow += '<div class="greybox ">'
                            + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + OnlySellView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'details\',event)">'
                            + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                            + '<div class="ruppee" id="othrFreOptMaxProfit">'
                            + '<span class="ruppeeMaxprofit" >₹' + Math.round(OnlySellView[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + OnlySellView[i].maxProfit + '</span>'
                                    + '<span class="requiredfundsotherdefault">' + OnlySellView[i].requiredFunds  + '</span></div > '
                             + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                            + '<div class="pairname" id="othrFreOptdesc"><b>' + OnlySellView[i].symbol + '</b>' + '&nbsp;' + OnlySellView[i].description + '</div></div>'
                            + '<div class="innerwhite">';
                        if (isRecommended) {
                            OnlySellViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                        }
                        OnlySellViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                            + '<span class="requiredfundsother">₹ ' + Math.round(OnlySellView[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                            + '<div class="twoblockcust mtop5"><div class="column">'
                            + '<div class="counterblock white other " id="cutinput">'
                            + '<div class="input-group">'
                            + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                            + '<div class="holder">'
                            + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + OnlySellView[i].id + '" > <span class="ltsize">Lot</span></div>'
                            + '<input  type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                            + '<div class="column text-right"><a  href="#confirmorder" onclick="GetStrategyDetails(' + OnlySellView[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'trade\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                                //+ '<small>' + OnlySellView[i].tradeCount + ' user traded</small></div></div>'
    
                        if (OnlySellView[i].tradeCount > 0) {
                            OnlySellViewRow += '<div class="tradedvalue">'
                                + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                + '<path data-name="Path 8"'
                                + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                + 'style="fill:#ff881c" ></path></svg>';
                            OnlySellViewRow += '<small>' + OnlySellView[i].tradeCount + ' user traded</small></div>';
                        }
                        OnlySellViewRow += '</div>';
    
                        $("#OtherFreeOptionsStrategiespanelfive").html(OnlySellViewRow);
    
                    }
                    if (OnlySellViewlen > 3) {
                        $("#btnViewMore").show();
                        $("#btnViewMore").click(function () { DashboardOnlySell(OnlySellViewlen) });
    
                    }
    
                }
            }
    
        }
    
    
        function GetStrategyDetails(id, potType, lots, source = 'INVESTOR', Staturgy, Submenu, action, maxlot, e) {
            debugger;
            var lotcount = $("#qty_" + id).val();
    
            var reqdata = ('{id:"' + id + '",potType:"' + potType + '",lots:"' + Number(lotcount) + '",Staturgy:"' + Staturgy + '",Submenu:"' + Submenu + '" ,source:"INVESTOR",subpot:0}');
            var data = EncryptData(reqdata);
            //console.clear();
            //console.log(reqdata);
            //console.log(data);
            $.ajax({
                type: "GET",
                url: '/Home/GetStrategyDetails?encKey=' + data.encKey + '&encData=' + data.encData,
                async: false,
                contentType: 'application/json; charset=utf-8',
                dataType: "text",
                //dataType: "html",
                success: function (response) {
                    var Strategy = JSON.parse(response);
                    //debugger;
                    //console.log(Strategy)
                    //  NSE_FO	2
                    //  NSE_CD	3
                    //if ((Strategy.data.legs[0].scrip.exchange == 2 && IsFnOActivated == 'Y' && action == 'details') || (Strategy.data.legs[0].scrip.exchange == 6 && IsFnOActivated == 'Y' && action == 'details') || (Strategy.data.legs[0].scrip.exchange == 3 && IsCDActivated == 'Y' && action == 'details') ){
                    if (action == 'details')
                    {
                        if ((Strategy.data.legs[0].scrip.exchange == 2 && IsFnOActivated == 'Y' && action == 'details') || (Strategy.data.legs[0].scrip.exchange == 6 && IsFnOActivated == 'Y' && action == 'details') || (Strategy.data.legs[0].scrip.exchange == 3 && IsCDActivated == 'Y' && action == 'details')) {
    
                            var URL = ParentURL + '/Option/GetStrategyDetails?encKey=' + data.encKey + '&encData=' + data.encData;
    
                         $("#strategiesslide").html('<iframe id="StrategyDetailsFrame" target="_parent"  src="' + URL + '" style="min-width:100%; min-height: 100%;" frameBorder="0"></iframe>');
                         $('#strategiesslide').addClass("open");
                         $('body').addClass("act");
                         $('body').css('overflow', 'hidden');
                        window.addEventListener('message', (event) => {
                            if (event.data.action)
                            {
                                //alert(event.data.action);
                                if (event.data.action == 'closeStrategyDetails') {
                                    $("#strategiesslide").removeClass("open");
                                    $("body").removeClass("act");
                                    $('body').css('overflow', 'scroll');
                                }else if (event.data.action == 'placeOrder') {
                                    $("#strategiesslide").removeClass("open");
                                    $("body").removeClass("act");
                                    $('body').css('overflow', 'scroll');
                                        GetStrategyDetails(id, potType, lots, source = 'INVESTOR',Staturgy, Submenu, 'trade', e);
                                }
                                else if (event.data.action == 'tradeparameters') {
                                    location.href = '#tradeparameters';
                                    $('#tradeparameters').addClass('overlay');
                                    $('#tradeparameters').show();
                                }
                                else if (event.data.action == 'RequiredFundTrade') {
                                    location.href = '#RequiredFundTrade';
                                    $('#RequiredFundTrade').addClass('overlay');
                                    $('#RequiredFundTrade').show();
                                }
                            }
                    });
                        }
                        else {
                            try {
                                clevertap.event.push("Web_activate_derivatives", {
                                    "Source": "Investert Home Page",
                                    "Date": new Date()
    
                                });
                            }
                            catch (err) {
                                CreateCleverTapLog("Web_activate_derivatives")
                            }
    
                            e.preventDefault();
    
                            location.href = "#";
    
                            location.href = "#activateoptions";
                        }
                    }
                    else if ((Strategy.data.legs[0].scrip.exchange == 2 && IsFnOActivated == 'Y' && action == 'trade') || (Strategy.data.legs[0].scrip.exchange == 6 && isMCXActivated == 'Y' && action == 'trade') || (Strategy.data.legs[0].scrip.exchange == 3 && IsCDActivated == 'Y' && action == 'trade')) {
                         var URL = ParentURL + '/Option/TradeConfirmOverlays?encKey=' + data.encKey + '&encData=' + data.encData;
                         location.href = "#confirmorder";
                         $("#confirmorder").html('<iframe id="StrategyTradeFrame" target="_parent"  src="' + URL + '" style="min-width:100%; min-height: 100%;" frameBorder="0"></iframe>');
                         //$("#confirmorder").html('<object type="text/html" style="height:100% !important; width:100% !important;" src="B" data="' + URL + '">');
                         $('#confirmorder').addClass("open");
                         $('#confirmorder').addClass("overlay");
                         $('body').addClass("act");
                         $('body').css('overflow', 'hidden');
                         window.addEventListener('message', (event) => {
    
                             if (event.data.action) {
                                 //alert(event.data.action);
                                 if (event.data.action == 'closeOrderForm') {
                                     $("#confirmorder").removeClass("open");
                                     $("#confirmorder").removeClass("overlay");
                                     $("body").removeClass("act");
                                     $('body').css('overflow', 'scroll');
                                     $("#confirmorder").html('');
                                 }
                                 else if (event.data.action == 'orderPlaced') {
                                         $("#confirmorder").removeClass("open");
                                         $("#confirmorder").removeClass("overlay");
                                     $("body").removeClass("act");
                                     $('body').css('overflow', 'scroll');
                                         $("#confirmorder").html('');
                                     }
                             }
                         });
                    }
    
                    else {
    
                        try {
                            clevertap.event.push("Web_activate_derivatives", {
                                "Source": "Investert Home Page",
                                "Date": new Date()
    
                            });
                        }
                        catch (err) {
                            CreateCleverTapLog("Web_activate_derivatives")
                        }
    
                         e.preventDefault();
    
                         location.href = "#";
    
                        location.href = "#activateoptions";
                    }
    
    
                    //IsFnOActivated == 'Y' && IsCDActivated == 'Y'
                }
            });
    
            //var URL = 'http://192.168.47.42:85/OptionDabbler/Option/GetStrategyDetails?encKey=' + data.encKey + '&encData=' + data.encData;
            ////console.log(URL)
            //$("#strategiesslide").html('<object type="text/html" style="min-width:102%; min-height: 800px;" src="B" data="' + URL + '">');
            //$('#strategiesslide').addClass("open");
    
            //$.ajax({
            //    type: "GET",
            //    url: "http://192.168.47.42:85/OptionDabbler/Option/StrategyDetails",
            //    data: data,
            //    dataType: "html",
            //    contentType: 'application/json; charset=utf-8',
            //    success: function (data) {
            //        console.log(data);
    
            //        if (data != null) {
            //            if (source == "InvestorWeb") {
            //               // $('#dvOptionLoader').hide();
            //                $('#strategiesslide').html('');
            //                $('#strategiesslide').html(data);
            //                childTab = "StrategyDetail";
            //                $('body').addClass("act");
            //                $('#strategiesslide').addClass("open");
            //            }
            //        }
    
            //        //$('#alldetails').addClass('open');
            //    },
            //    error: function () {
            //        $('#dvOptionLoader').hide();
            //        alert("error");
            //    }
            //});
        }
        function CloseStrategyDetails() {
            $('#strategiesslide').removeClass("open");
            $("body").removeClass("act");
            $('body').css('overflow', 'scroll');
        }
        function CloseOrderConfirm() {
            $('#strategiesslide').removeClass("open");
            $("body").removeClass("act");
            $('body').css('overflow', 'scroll');
        }
        function removeSeparator(str) {
        str = str.replace(/,/g, "");
        return str;
        }
        function OptionStoreCreateSession() {
                var clientCode = 'EBOM907310';
            var fullname = 'EBOM907310';
                var phone = '7071845054';
                var email = 'MAURYAMANISH5122000@GMAIL.COM';
                var BToken = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1bmlxdWVfbmFtZSI6IkVCT005MDczMTAiLCJyb2xlIjoiVCIsImFwcGlkIjoiM0Y1QjczRjktQTA3Ri00QUI5LTk2NzgtMDkxMzNBOTkyODJBIiwiZmxhZ3MiOiI0MTE0IiwidXNydGtuIjoiTEdjYTk0eWFHM0NVM2UxZnhSdzdhbVJLN1lQdGJsbEtVckwxMXJLbmMvNFBua1hEZENieGVlVFpWOG5DYVZZYiIsInVjaWQiOiI0ODA5NjY4IiwibmJmIjoxNzAwMTU0MTI2LCJleHAiOjE3MDAxNTg2MjYsImlhdCI6MTcwMDE1NTAyNiwiaXNzIjoibG9naW5fYXBpIiwiYXVkIjoidHJhZGluZ19hcGlzIn0.y9xe944GRhC9ZrhZa3SF8thjWaEQ0PvLat1ArQIbLU3maJs-W5TjNio7E2ZI5-94C9cL_drgxH4eMaExPmG7tgxBnWyMPvJUlCPFGqNUR806Zpkd2GVm8PilwXBxVDQqwKNcJDiRmPZ49PdUQHJy5evG6gaVkRtSjF5dsBWnkJgnTAmDLBAqKFKvSHJ3oBlofIsJq-Fg-B8JBChq8uoFVGenHzYZNRKccD8DsgcnT3e0DcIwhukwO-o07MUO45ls8IWgMhQnYfwsT7Vr3TgM0euyzCMakDMwL68fMh45VrmKpCXTmIqAdp82Q5JWeI7elLlpMqUnzrD0s0t8Ho2WdQ';
                var isFnOActivated = 'N';
                var isCDActivated = 'N';
    
                var recData = EncryptData(('{clientCode:"' + clientCode + '",fullname:"' + fullname + '",phone:"' + phone + '",appType:"InvestorWeb",Platform:"Non-Investor-Web",Email:"' + email + '",BToken:"' + BToken + '",isFnoActivated:"' + isFnOActivated + '",isCDActivated:"' + isCDActivated + '"}'));
                var URL_CP_dummy = 'https://invest.motilaloswal.com/OptionDabbler/Option/CreateInvestorSession?' + 'encKey=' + recData.encKey + '&encData=' + recData.encData;
            $("#hiddendiv").html('');
            var parent = document.getElementById('hiddendiv');
                var iDiv = document.createElement('div');
                iDiv.className = "main-container";
                var vDiv = document.createElement('div');
                vDiv.id = "content";
                vDiv.className = "container";
                vDiv.style = "overflow:hidden;height:0px;";
                iDiv.appendChild(vDiv);
                parent.appendChild(iDiv);
    
                // $('#hiddendiv').addClass('Container');
            $("#content").html('<object type="text/html" style="border:1px solid red; min-height: 0px; max-height:0px !importan; " src="B" data="' + URL_CP_dummy + '">');
        }
        function SendScripsToBServerFromStrategy(exchCode, ScripCode) {
            SendToBServer(CreateScripDatabyExchCode(exchCode, ScripCode, "1"));
        }
        function SetLTPStrategyDetailsTab(idName, LTP, ChangePer, Change ) {
            var iframeDetails = document.getElementById("StrategyDetailsFrame");
            var iframeTrade = document.getElementById("StrategyTradeFrame");
            //iframe.contentWindow.TestAlert()
            if (Array.from(idName)[0] == '3') {
                ChangePer = Number(ChangePer).toFixed(2);
            }
            if (iframeDetails != undefined) {
                iframeDetails.contentWindow.setLTPChange(idName, LTP, Change,ChangePer);
            } if (iframeTrade != undefined) {
                iframeTrade.contentWindow.setLTPChange(idName, LTP, Change,ChangePer);
            }
        }
    
        var STARTERViewRowViewmore = '';
        var REQFundless10KViewrowViewmore = '';
        var MAXLOSS2KViewRowViewmore = '';
        var MultilegViewRowViewmore = '';
        var OnlySellViewRowViewmore = '';
    
        var MultilegViewRowCount = '';
        var STARTERViewRowcount = '';
        var OnlySellViewRowcount = '';
        var REQFundless10KViewrowcount = '';
        var MAXLOSS2KViewRowcount = '';
    
    
        function LoadFreePotsOnHome(Value, Source) {
            $("#one-tab").hide();
            $("#two-tab").hide();
            $("#three-tab").hide();
            $("#four-tab").hide();
            $("#five-tab").hide();
            $("#btnViewMore").hide();
            STARTERViewRowViewmore = '';
            REQFundless10KViewrowViewmore = '';
            MAXLOSS2KViewRowViewmore = '';
            MultilegViewRowViewmore = '';
            OnlySellViewRowViewmore = '';
    
            MultilegViewRowCount = '';
            STARTERViewRowcount = '';
            OnlySellViewRowcount = '';
            REQFundless10KViewrowcount = '';
            MAXLOSS2KViewRowcount = '';
    $("#OtherFreeOptionsStrategiespanelfive").empty();
    $("#OtherFreeOptionsStrategiespanelfour").empty();
    $("#OtherFreeOptionsStrategiespanelthree").empty();
    $("#OtherFreeOptionsStrategiespaneltwo").empty();
    $("#OtherFreeOptionsStrategies").empty();
    var filterValueStarter = '';
    var filterValuREQFundless10K = '';
    var filterValueMultileg = '';
    var filterValueMaxLoss2K = '';
    var filterValueOnlysell = '';
    var FilterViewRow = '';
    
    var STARTERViewRow = '';
    var REQFundless10KViewrow = '';
    var MAXLOSS2KViewRow = '';
    var MultilegViewRow = '';
    var OnlySellViewRow = '';
    
    
    var One = '';
    var two = '';
    var three = '';
    var four = '';
            var five = '';
    
            STARTERViewRowViewmore = 1;
            MultilegViewRowCount = 1;
            STARTERViewRowcount = 1;
            OnlySellViewRowcount = 1;
            REQFundless10KViewrowcount = 1;
            MAXLOSS2KViewRowcount = 1;
    //debugger;
    var Instrument = Value
            var Sourcevalue = Source
    
         
    
            var para = {
                ConditionID: Starterid,
                Conditioname: Startercondition,
                FilterName: Instrument,
            };
    
            var datapara = EncryptData(JSON.stringify(para));
            var res = ajaxCall('POST', '/Home/GetStrategiesDataFromFilter', datapara, false);
    
            if (res.data != null)
            {
                if (res.data.filters != null)
                {
                    for (var i = 0; i < res.data.filters.length; i++) {
                        switch (res.data.filters[i].id) {
                            case "Starter":
                                Starterid = res.data.filters[i].id;
                                Startercondition = res.data.filters[i].condition;
                                filterValueStarter = res.data.filters[i].filterValue;
                                $("#one-tab").html(res.data.filters[i].label);
                                $("#one-tab").show();
                                One = "1";
                                break;
                            case "Margin10K":
                                Margin10Kid = res.data.filters[i].id;
                                Margin10Kidcondition = res.data.filters[i].condition;
                                filterValuREQFundless10K = res.data.filters[i].filterValue;
                                $("#two-tab").html(res.data.filters[i].label);
                                $("#two-tab").show();
                                two = '1';
                                break;
                            case "MaxLoss2K":
                                MaxLossId = res.data.filters[i].id;
                                MaxLossIdcondition = res.data.filters[i].condition;
                                filterValueMaxLoss2K = res.data.filters[i].filterValue;
                                $("#three-tab").html(res.data.filters[i].label);
                                $("#three-tab").show();
                                three = '1';
                                break;
                            case "Strategy":
                                StrategyMultileg = res.data.filters[i].id;
                                StrategyMultilegcondition = res.data.filters[i].condition;
                                filterValueMultileg = res.data.filters[i].filterValue;
                                $("#four-tab").html(res.data.filters[i].label);
                                $("#four-tab").show();
                                four = '1';
                                break;
                            case "OnlySell":
                                OnlySellID = res.data.filters[i].id;
                                OnlySellcondition = res.data.filters[i].condition;
                                filterValueOnlysell = res.data.filters[i].filterValue;
                                $("#five-tab").html(res.data.filters[i].label);
                                $("#five-tab").show();
                                five = '1';
                                break;
                            default: break;
                        }
                    }
    
                }
    
                FilterViewRow = res.data.calls;
                var FilterViewlen = FilterViewRow.length;
                if (FilterViewlen > 0)
                {
                    for (let i = 0; i < FilterViewlen; i++) {
                        if (filterValueStarter != '') {
                            if ((FilterViewRow[i].filterFlag & filterValueStarter) ? true : false == true)
                            {
    
                                {
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    STARTERViewRowViewmore += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        STARTERViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    STARTERViewRowViewmore += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                        + '<div class="holder">'
                                        + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '"> <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        STARTERViewRowViewmore += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        STARTERViewRowViewmore += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    STARTERViewRowViewmore += '</div>';
    
                                    
                                }
    
                                if (STARTERViewRowcount <= 3)
                                {
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    STARTERViewRow += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        STARTERViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    STARTERViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                        + '<div class="holder">'
                                        + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '"> <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'STARTER\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        STARTERViewRow += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        STARTERViewRow += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    STARTERViewRow += '</div>';
    
                                    $("#OtherFreeOptionsStrategies").html(STARTERViewRow);
                                }
                                STARTERViewRowcount++
    
                                if ((STARTERViewRowcount -1) > 3)
                                {
                                    $("#btnViewMore").show();
                                    $("#btnViewMore").click(function () { OnStarterViewMoreClick() });
    
                                }
                            }
    
                        }
                        if (filterValuREQFundless10K != '') {
                            if ((FilterViewRow[i].filterFlag & filterValuREQFundless10K) ? true : false == true)
                            {
                                {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    REQFundless10KViewrowViewmore += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        REQFundless10KViewrowViewmore += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    REQFundless10KViewrowViewmore += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                        + '<div class="holder">'
                                        + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '"> <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        REQFundless10KViewrowViewmore += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        REQFundless10KViewrowViewmore += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    REQFundless10KViewrowViewmore += '</div>';
    
                                }
    
                                if (REQFundless10KViewrowcount <= 3) {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    REQFundless10KViewrow += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        /*+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '*/
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        REQFundless10KViewrow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    REQFundless10KViewrow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);" >'
                                        + '<div class="holder">'
                                        + '<input onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '"> <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" class="cta trades custom"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'REQ FUNDS <10K\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        REQFundless10KViewrow += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        REQFundless10KViewrow += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    REQFundless10KViewrow += '</div>';
    
                                    $("#OtherFreeOptionsStrategiespaneltwo").html(REQFundless10KViewrow);
                                }
    
                                REQFundless10KViewrowcount++
                                if ((REQFundless10KViewrowcount -1) > 3) {
                                  $("#btnViewMore").show();
                                    $("#btnViewMore").click(function () { OnREQFundless10KViewMoreClick() });
    
                                }
                            }
                        }
                        if (filterValueMaxLoss2K != '') {
                            if ((FilterViewRow[i].filterFlag & filterValueMaxLoss2K) ? true : false == true)
                            {
    
                                {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    MAXLOSS2KViewRowViewmore += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        MAXLOSS2KViewRowViewmore += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    MAXLOSS2KViewRowViewmore += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        MAXLOSS2KViewRowViewmore += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        MAXLOSS2KViewRowViewmore += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    MAXLOSS2KViewRowViewmore += '</div>';
    
    
                                }
    
                                if(MAXLOSS2KViewRowcount <= 3)
                                {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    MAXLOSS2KViewRow += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        MAXLOSS2KViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    MAXLOSS2KViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'MAX LOSS < 2K\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        MAXLOSS2KViewRow += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        MAXLOSS2KViewRow += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    MAXLOSS2KViewRow += '</div>';
    
                                    $("#OtherFreeOptionsStrategiespanelthree").html(MAXLOSS2KViewRow);
    
                                }
                                MAXLOSS2KViewRowcount++
                                if ((MAXLOSS2KViewRowcount -1) > 3) {
                                    $("#btnViewMore").show();
                                    $("#btnViewMore").click(function () { OnMAXLOSS2KViewMoreClick() });
    
                                }
                            }
    
                        }
                        if (filterValueMultileg != '') {
                            if ((FilterViewRow[i].filterFlag & filterValueMultileg) ? true : false == true)
                            {
    
    
                                {
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    MultilegViewRowViewmore += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        MultilegViewRowViewmore += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    MultilegViewRowViewmore += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity" onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)"  class="cta trades custom">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        MultilegViewRowViewmore += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        MultilegViewRowViewmore += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    MultilegViewRowViewmore += '</div>';
    
                                }
    
                                if (MultilegViewRowCount <= 3)
                                {
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    MultilegViewRow += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        MultilegViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    MultilegViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input type = "button" class="button-plusother" data-field="quantity" onclick="incrementValuother(event)" ></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Multileg\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)"  class="cta trades custom">Trade</a></div></div></div>';
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        MultilegViewRow += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        MultilegViewRow += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    MultilegViewRow += '</div>';
    
                                    $("#OtherFreeOptionsStrategiespanelfour").html(MultilegViewRow);
                                }
                                MultilegViewRowCount++
                                if ((MultilegViewRowCount -1) > 3) {
                                    $("#btnViewMore").show();
                                    $("#btnViewMore").click(function () { OnMultilegViewMoreClick() });
    
                                }
                            }
                        }
                        if (filterValueOnlysell != '') {
                            if ((FilterViewRow[i].filterFlag & filterValueOnlysell) ? true : false == true)
                            {
    
                                {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    OnlySellViewRowViewmore += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        OnlySellViewRowViewmore += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    OnlySellViewRowViewmore += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input  type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                                    //+ '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div></div>'
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        OnlySellViewRowViewmore += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        OnlySellViewRowViewmore += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    OnlySellViewRowViewmore += '</div>';
    
    
                                }
    
                                if (OnlySellViewRowcount <= 3) {
    
                                    FilterViewRow[i].maxProfit = Math.round(FilterViewRow[i].maxProfit);
                                    FilterViewRow[i].requiredFunds = Math.round(FilterViewRow[i].requiredFunds);
                                    var Recommendstatus = ''
                                    var isRecommended = FilterViewRow[i].isRecommended;
                                    if (isRecommended == false) {
    
                                        Recommendstatus = '';
                                    }
                                    else {
                                        Recommendstatus = 'RECOMMENDED';
                                    }
    
                                    OnlySellViewRow += '<div class="greybox ">'
                                        + '<div class="innergrey openfreeslide"  onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'details\',\'' + FilterViewRow[i].maxLotSize + '\',event)">'
                                        + '<div class="tpsection"><div class="left"><span>Max Profit</span>'
                                        + '<div class="ruppee" id="othrFreOptMaxProfit">'
                                        + '<span class="ruppeeMaxprofit" >₹' + Math.round(FilterViewRow[i].maxProfit).toLocaleString('en-IN') + '</span ></div></div>'
                                        + '<div class="hiddendefaultvalues" style="display:none"><span class="ruppeeMaxprofitdefault">' + FilterViewRow[i].maxProfit + '</span>'
                                        //+ '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span><span class="maxLotSizeOther">' + FilterViewRow[i].maxLotSize + '</span></div > '
                                        + '<span class="requiredfundsotherdefault">' + FilterViewRow[i].requiredFunds + '</span>'
                                        + '<span class="maxLotSizeOther" > ' + FilterViewRow[i].maxLotSize + '</span >'
                                        + '<span class="symbolOther">' + FilterViewRow[i].symbol + '</span>'
                                        + '<span class="lotSizeOther">' + FilterViewRow[i].lotSize + '</span></div >'
                                        + '<div class="right"><img src="/Images/toparrow.png" alt=""></div></div>'
                                        + '<div class="pairname" id="othrFreOptdesc"><b>' + FilterViewRow[i].symbol + '</b>' + '&nbsp;' + FilterViewRow[i].description + '</div></div>'
                                        + '<div class="innerwhite">';
                                    if (isRecommended) {
                                        OnlySellViewRow += '<div class="recommended"><div class="redbox">' + Recommendstatus + '</div></div>';
                                    }
                                    OnlySellViewRow += '<small>Required Funds</small><div class="requiredfunds" id="othrFreOptreqdfunds">'
                                        + '<span class="requiredfundsother">₹ ' + Math.round(FilterViewRow[i].requiredFunds).toLocaleString('en-IN') + '</span></div > '
                                        + '<div class="twoblockcust mtop5"><div class="column">'
                                        + '<div class="counterblock white other " id="cutinput">'
                                        + '<div class="input-group">'
                                        + '<input type = "button" class="button-minusother" data-field="quantity" onclick="decrementValueother(event);"  >'
                                        + '<div class="holder">'
                                        + '<input  onchange="updateRatesOther(event)" type="number" step="1" max="" value="1" name="quantity" class="quantity-field" id="qty_' + FilterViewRow[i].id + '" > <span class="ltsize">Lot</span></div>'
                                        + '<input  type = "button" class="button-plusother" data-field="quantity"  onclick="incrementValuother(event)"></div></div></div>'
                                        + '<div class="column text-right"><a  href="#confirmorder" onclick="GetStrategyDetails(' + FilterViewRow[i].id + ', 1, 1,\'INVESTOR\',\'Other Free Options Strategies\',\'Only Sell\',\'trade\',\'' + FilterViewRow[i].maxLotSize + '\',event)" class="cta trades custom">Trade</a></div></div></div>';
    
                                    //+ '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div></div>'
    
                                    if (FilterViewRow[i].tradeCount > 0) {
                                        OnlySellViewRow += '<div class="tradedvalue">'
                                            + '<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24">'
                                            + '<path data-name="Path 7" d="M0 0h24v24H0z" style="fill:none" ></path>'
                                            + '<path data-name="Path 8"'
                                            + 'd="M16 11a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm-8 0a3 3 0 1 0-3-3 2.987 2.987 0 0 0 3 3zm0 2c-2.33 0-7 1.17-7 3.5V19h14v-2.5c0-2.33-4.67-3.5-7-3.5zm8 0c-.29 0-.62.02-.97.05A4.22 4.22 0 0 1 17 16.5V19h6v-2.5c0-2.33-4.67-3.5-7-3.5z"'
                                            + 'style="fill:#ff881c" ></path></svg>';
                                        OnlySellViewRow += '<small>' + FilterViewRow[i].tradeCount + ' user traded</small></div>';
                                    }
                                    OnlySellViewRow += '</div>';
    
                                    $("#OtherFreeOptionsStrategiespanelfive").html(OnlySellViewRow);
    
                                }
    
                                OnlySellViewRowcount++
                                if ((OnlySellViewRowcount -1)> 3) {
                                    $("#btnViewMore").show();
                                    $("#btnViewMore").click(function () { OnlySellViewMoreClick() });
    
                                }
                            }
                        }
                    }
                }
                else {
                    $('#dvOptionLoader').hide();
                    $("#one-panel").hide();
                    $("#two-panel").hide();
                    $("#three-panel").hide();
                    $("#four-panel").hide();
                    $("#five-panel").hide();
                    $("#fivea-panel").show();
                    document.getElementById("one-tab").className = 'hidden';
                    document.getElementById("two-tab").className = 'hidden';
                    document.getElementById("three-tab").className = 'hidden';
                    document.getElementById("four-tab").className = 'hidden';
                    document.getElementById("five-tab").className = 'hidden';
                    var OtherFreeOptionsStrategiespanelNorecord = '';
                    $("#OtherFreeOptionsStrategiespanelNorecord").html("");
                    OtherFreeOptionsStrategiespanelNorecord = '';
                    OtherFreeOptionsStrategiespanelNorecord += '<div style="margin-left: 500px;">'
                        + '<svg xmlns = "http://www.w3.org/2000/svg" width = "70" height = "70" viewBox = "0 0 96 96" > '
                        + '<g data-name="Group 16975">'
                        + '<path data-name="Rectangle 463" style="fill:none" d="M0 0h96v96H0z"></path>'
                        + '<g data-name="Group 16738">'
                        + '<g data-name="Group 15779">'
                        + '<path data-name="Path 3322" d="M.325.759 79.01.772v1.722L.325 2.558z"'
                        + 'transform="translate(8.23 12.989)" style="fill:#2c3949"></path>'
                        + '<path data-name="Path 3320"'
                        + 'd="M112.687 75.09c9.326 20.958 8.345 48.07-3.179 67.81l-.034 4.291h-8.008V142.9H48.745v4.291h-8.008L40.7 142.9c-11.519-19.74-12.5-46.852-3.174-67.81z"'
                        + 'transform="translate(-27.219 -59.638)" style="fill:#f5f5f5;fill-rule:evenodd">'
                        + '</path>'
                        + '<path data-name="Path 3321"'
                        + 'd="M61.452 0H135.7c5.551 0 5.551 5.942 0 5.942H61.452c-5.588 0-5.588-5.942 0-5.942z"'
                        + 'transform="translate(-50.677 8)" style="fill:#f5f5f5;fill-rule:evenodd"></path></g>'
                        + '<text data-name="₹" transform="translate(35 25)"'
                        + 'style="fill:#b7b4b4;font-size:40px;font-family:FiraSans-SemiBold,Fira Sans;font-weight:600">'
                        + '<tspan x="0" y="37" style="font-size: 40px">₹</tspan>'
                        + '</text></g></g></svg>'
                        + '<svg xmlns = "http://www.w3.org/2000/svg" width = "100" height = "100" viewBox = "0 0 96 96" > <g data-name="Group 16975"><path data-name="Rectangle 463" style="fill:none" d="M0 0h96v96H0z"></path><g data-name="Group 16738"><g data-name="Group 15779"><path data-name="Path 3322" d="M.325.759 79.01.772v1.722L.325 2.558z" transform="translate(8.23 12.989)" style="fill:#2c3949"></path><path data-name="Path 3320" d="M112.687 75.09c9.326 20.958 8.345 48.07-3.179 67.81l-.034 4.291h-8.008V142.9H48.745v4.291h-8.008L40.7 142.9c-11.519-19.74-12.5-46.852-3.174-67.81z" transform="translate(-27.219 -59.638)" style="fill:#f5f5f5;fill-rule:evenodd"></path><path data-name="Path 3321" d="M61.452 0H135.7c5.551 0 5.551 5.942 0 5.942H61.452c-5.588 0-5.588-5.942 0-5.942z" transform="translate(-50.677 8)" style="fill:#f5f5f5;fill-rule:evenodd"></path></g><text data-name="₹" transform="translate(35 25)" style="fill: #b7b4b4;font-size:40px;font-family:FiraSans-SemiBold,Fira Sans;font-weight:600"><tspan x="0" y="37" style="font-size: 40px">₹</tspan></text></g></g></svg >'
                        + '</div> '
                        + '<span style="padding-top: 100px;margin-left: -275px;color: #959595;"> We don’t have Other Free Options Strategies at this moment!</span >'
                    $("#OtherFreeOptionsStrategiespanelNorecord").html(OtherFreeOptionsStrategiespanelNorecord);
                }
                if (One != '') {
                    $("#OtherFreeOptionsStrategies").show();
                    $("#OtherFreeOptionsStrategiespaneltwo").hide();
                    $("#OtherFreeOptionsStrategiespanelthree").hide();
                    $("#OtherFreeOptionsStrategiespanelfour").hide();
                    $("#OtherFreeOptionsStrategiespanelfive").hide();
                    if (STARTERViewRowcount <= 3) {
                        $("#btnViewMore").show();
                    }
                    else {
                        $("#btnViewMore").show();
                    }
                    $("#opstrategy").show();
                   // DashboardSTARTERNew();
                    $("#one-tab").click();
    
                    
                }
                else if (two != '') {
                    $("#OtherFreeOptionsStrategies").hide();
                    $("#OtherFreeOptionsStrategiespaneltwo").show();
                    $("#OtherFreeOptionsStrategiespanelthree").hide();
                    $("#OtherFreeOptionsStrategiespanelfour").hide();
                    $("#OtherFreeOptionsStrategiespanelfive").hide();
                    if (REQFundless10KViewrowcount <= 3) {
                        $("#btnViewMore").hide();
                    } else {
                        $("#btnViewMore").show();
                    }
                    $("#opstrategy").show();
                    //DashboardREQFundless10KNew();
                    $("#two-tab").click();
                   
                }
                else if (three != '')
                {
                    $("#OtherFreeOptionsStrategies").hide();
                    $("#OtherFreeOptionsStrategiespaneltwo").hide();
                    $("#OtherFreeOptionsStrategiespanelthree").show();
                    $("#OtherFreeOptionsStrategiespanelfour").hide();
                    $("#OtherFreeOptionsStrategiespanelfive").hide();
                    if (MAXLOSS2KViewRowcount <= 3) {
                        $("#btnViewMore").hide();
                    } else {
                        $("#btnViewMore").show();
                    }
                    $("#opstrategy").show();
                    //DashboardMAXLOSS2KNew();
                    $("#three-tab").click();
                    
                }
                else if (four != '')
                {
                    
                    $("#OtherFreeOptionsStrategies").hide();
                    $("#OtherFreeOptionsStrategiespaneltwo").hide();
                    $("#OtherFreeOptionsStrategiespanelthree").hide();
                    $("#OtherFreeOptionsStrategiespanelfour").show();
                    $("#OtherFreeOptionsStrategiespanelfive").hide();
                    if (MultilegViewRowCount <= 3) {
                        $("#btnViewMore").hide();
                    } else {
                        $("#btnViewMore").show();
                    }
                    $("#opstrategy").show();
    
                    $("#four-tab").click();
                   
                }
                else if (five != '')
                {
                    $("#OtherFreeOptionsStrategies").hide();
                    $("#OtherFreeOptionsStrategiespaneltwo").hide();
                    $("#OtherFreeOptionsStrategiespanelthree").hide();
                    $("#OtherFreeOptionsStrategiespanelfour").hide();
                    $("#OtherFreeOptionsStrategiespanelfive").show();
                    if (OnlySellViewRowcount <= 3) {
                        $("#btnViewMore").hide();
                    } else {
                        $("#btnViewMore").show();
                    }
                   // DashboardOnlySellNew();
                    $("#five-tab").click();
                }
                $("#opstrategy").show();
                
            }
        }
    
        function DashboardSTARTERNew() {
            //debugger;
            $("#OtherFreeOptionsStrategies").show();
            $("#OtherFreeOptionsStrategiespaneltwo").hide();
            $("#OtherFreeOptionsStrategiespanelthree").hide();
            $("#OtherFreeOptionsStrategiespanelfour").hide();
            $("#OtherFreeOptionsStrategiespanelfive").hide();
            if ((STARTERViewRowcount -1) <= 3) {
                $("#btnViewMore").hide();
            } else {
                $("#btnViewMore").show();
            }
            $("#OtherFreeOptionsStrategiesViewmore").hide();
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home",
                    "Tab Name": "STARTER",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
        function DashboardREQFundless10KNew() {
            //debugger;
            $("#OtherFreeOptionsStrategies").hide();
            $("#OtherFreeOptionsStrategiespaneltwo").show();
            $("#OtherFreeOptionsStrategiespanelthree").hide();
            $("#OtherFreeOptionsStrategiespanelfour").hide();
            $("#OtherFreeOptionsStrategiespanelfive").hide();
            if ((REQFundless10KViewrowcount -1) <= 3) {
                $("#btnViewMore").hide();
            } else {
                $("#btnViewMore").show();
            }
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home",
                    "Tab Name": "REQ FUNDS LESS THAN 10K",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
        function DashboardMAXLOSS2KNew() {
            //debugger;
            $("#OtherFreeOptionsStrategies").hide();
            $("#OtherFreeOptionsStrategiespaneltwo").hide();
            $("#OtherFreeOptionsStrategiespanelthree").show();
            $("#OtherFreeOptionsStrategiespanelfour").hide();
            $("#OtherFreeOptionsStrategiespanelfive").hide();
            if ((MAXLOSS2KViewRowcount -1) <= 3) {
                $("#btnViewMore").hide();
            } else {
                $("#btnViewMore").show();
            }
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home",
                    "Tab Name": "MAX LOSS LESS THAN 2K",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
        function DashboardMultilegNew() {
            //debugger;
           
            $("#OtherFreeOptionsStrategies").hide();
            $("#OtherFreeOptionsStrategiespaneltwo").hide();
            $("#OtherFreeOptionsStrategiespanelthree").hide();
            $("#OtherFreeOptionsStrategiespanelfour").show();
            $("#OtherFreeOptionsStrategiespanelfive").hide();
            if ((MultilegViewRowCount -1)<= 3) {
                $("#btnViewMore").hide();
            } else {
                $("#btnViewMore").show();
            }
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home",
                    "Tab Name": "Multileg",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
        function DashboardOnlySellNew() {
            //debugger;
            $("#OtherFreeOptionsStrategies").hide();
            $("#OtherFreeOptionsStrategiespaneltwo").hide();
            $("#OtherFreeOptionsStrategiespanelthree").hide();
            $("#OtherFreeOptionsStrategiespanelfour").hide();
            $("#OtherFreeOptionsStrategiespanelfive").show();
            if ((OnlySellViewRowcount -1) <= 3) {
                $("#btnViewMore").hide();
            } else {
                $("#btnViewMore").show();
            }
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home",
                    "Tab Name": "Only Sell",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
    
        function OnStarterViewMoreClick() {
           // debugger;
            $("#OtherFreeOptionsStrategies").empty();
            $("#OtherFreeOptionsStrategies").html(STARTERViewRowViewmore)
            $("#OtherFreeOptionsStrategies").show();
    
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home ViewMore",
                    "Tab Name": "STARTER",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
           
        }
        function OnREQFundless10KViewMoreClick() {
           // debugger;
            $("#OtherFreeOptionsStrategiespaneltwo").empty();
            $("#OtherFreeOptionsStrategiespaneltwo").html(REQFundless10KViewrowViewmore)
            /*$("#OtherFreeOptionsStrategiespaneltwo").show();*/
    
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home ViewMore",
                    "Tab Name": "REQ FUNDS LESS THAN 10K",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
    
        }
        function OnMAXLOSS2KViewMoreClick() {
            //debugger;
            $("#OtherFreeOptionsStrategiespanelthree").empty();
            $("#OtherFreeOptionsStrategiespanelthree").html(MAXLOSS2KViewRowViewmore)
            /*$("#OtherFreeOptionsStrategiespanelthree").show();*/
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home ViewMore",
                    "Tab Name": "MAX LOSS LESS THAN 2K",
                    "Date": new Date()
                });
            }
    
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
    
        }
    
        function OnMultilegViewMoreClick() {
           /// debugger;
            $("#OtherFreeOptionsStrategiespanelfour").empty();
            $("#OtherFreeOptionsStrategiespanelfour").html(MultilegViewRowViewmore)
            //$("#OtherFreeOptionsStrategiespanelfour").show();
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home ViewMore",
                    "Tab Name": "Multileg",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
        }
        function OnlySellViewMoreClick() {
            //debugger;
            $("#OtherFreeOptionsStrategiespanelfive").empty();
            $("#OtherFreeOptionsStrategiespanelfive").html(OnlySellViewRowViewmore)
        /*   $("#OtherFreeOptionsStrategiespanelfive").show();*/
    
            try {
                clevertap.event.push("Web_options_store_category", {
                    "Source": "Invester Home ViewMore",
                    "Tab Name": "Only Sell",
                    "Date": new Date()
                });
            }
            catch (err) {
                CreateCleverTapLog("Web_options_store_category")
            }
    
        }
    


$(".select-wrap").select2();



        $(document).ready(function () {
            
            var table;
            if ($.fn.dataTable.isDataTable('#simple-data-table')) {
                table = $('#simple-data-table').DataTable();
            }
            else {
                table = $('#simple-data-table').DataTable({
                    searching: !1, bInfo: !1, lengthChange: !1, bPaginate: !1,  "order":[]
                });
            }
    
            table.rows().every(function () {
                var data = this.data();
                //setTimeout(function () {
                //    //alert("Reconnect");
                //}, 7000);
                
                //console.log(data);
                // UpdateMarketsData_Home(11508.55, 0, 10, 0, '01594', 2, 12.43, 128105);
                SendToBServer(CreateScripDatabyExchCode(data[5], data[6], "1"));
              
            });
        });
    
        function UpdateMarketsData_Home(rate, ATP, Volume, Value, IdName, dPoint, perChange, changeValue) {
            //var Volumeinlac = (Number(Volume) / 100000).toFixed(dPoint);
            var Volumeinlac = GetPriceSafix(Volume);
            var Valueinlac = GetPriceSafix(Number(Value * 100000));
            $('#' + IdName + 'LTPHomeGainerLoser').html(NumbersWithCommas(rate));
            $('#' + IdName + 'ATPHomeGainerLoser').html(ATP);
            $('#' + IdName + 'VolHomeGainerLoser').html(Volumeinlac);
            $('#' + IdName + 'ValHomeGainerLoser').html(Valueinlac);
            $('#' + IdName + 'CPerHomeGainerLoser').html(NumbersWithCommas(changeValue) + " (" + NumbersWithCommas(perChange) + "%)");
            if (perChange < 0) {
    
                $('#' + IdName + 'CPerHomeGainerLoser').css({ "color": "#EB6400" });
                $('#arrow_' + IdName).removeClass("green-arrow-vsmall");
                $('#arrow_' + IdName).addClass("red-arrow-vsmall");
                $('#' + IdName + 'CPerHomeGainerLoser').removeClass("green-text");
                $('#' + IdName + 'CPerHomeGainerLoser').addClass("red-text");
            }
            else if (perChange >= 0) {
    
                $('#' + IdName + 'CPerHomeGainerLoser').css({ "color": "#5EB73B" });
                $('#arrow_' + IdName).removeClass("red-arrow-vsmall");
                $('#arrow_' + IdName).addClass("green-arrow-vsmall");
                $('#' + IdName + 'CPerHomeGainerLoser').addClass("green-text");
                $('#' + IdName + 'CPerHomeGainerLoser').removeClass("red-text");
            }
        }
    



    
    function OpenLumpsum(id) {

        var type = $("#" + id).data("schemename");

        //try {
        //    // Particular event function for netcore integration - Vishal
        //    //alert(type);
        //    smartech('dispatch', 'MF_Lumpsum_OrderForm', {
        //        'scheme_name': type,
        //        'redirection_source': 'Home'
        //    });
        //}
        //catch (err) {
        //    console.log('Smarttech not initiated in MF_Lumpsum_OrderForm');
        //    createNetcoreLog('MF_Lumpsum_OrderForm');
        //}
        
        if (isGuestUser() == 1) { return false; }
        $("#dvLoader").show();
        var randomNum = Math.floor(Math.random() * (1000 - 10) + 10);
        var siplumpsumorder = {
            randomNumber: randomNum,
            isin: $("#" + id).data("isin"),
            schemecode: $("#" + id).data("schemecode"),
            schemename: $("#" + id).data("schemename"),
            fundtype: $("#" + id).data("fundtype"),
            token: $("#" + id).data("token"),
            nav: $("#" + id).data("nav"),
            navchange: $("#" + id).data("navchange"),
            navchangeper: $("#" + id).data("navchangeper"),
            navdate: $("#" + id).data("navdate"),
            formtitle: "Lumpsum",
            txnType: "FP"
        };
        $.post("/MutualFund/LUMPSUMForm", { sip_lumpsum_order: siplumpsumorder }, function (response) {
            var orderformname = "OrderFormMutualFundLumpsum_" + randomNum
            $("#lumpsumform").html(response);
            $("#" + orderformname).modal("show");
            $("#dvLoader").hide();
        });
    }

    function OpenSIP(id) {

        var type = $("#" + id).data("schemename");
        //try {
        //    // Particular event function for netcore integration - Vishal
        //    smartech('dispatch', 'MF_SIP_OrderForm', {
        //        'scheme_name': type,
        //        'redirection_source': 'Home'
        //    });
        //}
        //catch (err) {
        //    console.log('Smarttech not initiated in MF_SIP_OrderForm');
        //    createNetcoreLog('MF_SIP_OrderForm');
        //}
        
        if (isGuestUser() == 1) { return false; }
        $("#dvLoader").show();
        var randomNum = Math.floor(Math.random() * (1000 - 10) + 10);
        var siplumpsumorder = {
            randomNumber: randomNum,
            isin: $("#" + id).data("isin"),
            schemecode: $("#" + id).data("schemecode"),
            schemename: $("#" + id).data("schemename"),
            fundtype: $("#" + id).data("fundtype"),
            token: $("#" + id).data("token"),
            nav: $("#" + id).data("nav"),
            navchange: $("#" + id).data("navchange"),
            navchangeper: $("#" + id).data("navchangeper"),
            navdate: $("#" + id).data("navdate"),
            txnType: "SIP",
        };
        $.post("/MutualFund/SIPForm", { sip_lumpsum_order: siplumpsumorder }, function (response) {
            var orderformname = "OrderFormMutualFundSip_" + randomNum
            $("#sipform").html(response);
            $("#" + orderformname).modal("show");
            $("#dvLoader").hide();
        });
    }

    //$(".scannerSIP").click(function () {
    //    
    //    $("#dvLoader").show();
    //    var randomNum = Math.floor(Math.random() * (1000 - 10) + 10);
    //    var siplumpsumorder = {
    //        randomNumber: randomNum,
    //        isin: $("#" + $(this).attr('id')).data("isin"),
    //        schemecode: $("#" + $(this).attr('id')).data("schemecode"),
    //        schemename: $("#" + $(this).attr('id')).data("schemename"),
    //        fundtype: $("#" + $(this).attr('id')).data("fundtype"),
    //        token: $("#" + $(this).attr('id')).data("token"),
    //        nav: $("#" + $(this).attr('id')).data("nav"),
    //        navchange: $("#" + $(this).attr('id')).data("navchange"),
    //        navchangeper: $("#" + $(this).attr('id')).data("navchangeper"),
    //        navdate: $("#" + $(this).attr('id')).data("navdate"),
    //        txnType: "SIP"
    //    };
    //    $.post("/MutualFund/SIPForm", { sip_lumpsum_order: siplumpsumorder }, function (response) {
    //        var orderformname = "OrderFormMutualFundSip_" + randomNum
    //        $("#sipform").html(response);
    //        $("#" + orderformname).modal("show");
    //        $("#dvLoader").hide();
    //    });
    //});

    //$(".scannerLumpsum").click(function () {
    //    
    //    $("#dvLoader").show();
    //    var randomNum = Math.floor(Math.random() * (1000 - 10) + 10);
    //    var siplumpsumorder = {
    //        randomNumber: randomNum,
    //        isin: $("#" + $(this).attr('id')).data("isin"),
    //        schemecode: $("#" + $(this).attr('id')).data("schemecode"),
    //        schemename: $("#" + $(this).attr('id')).data("schemename"),
    //        fundtype: $("#" + $(this).attr('id')).data("fundtype"),
    //        token: $("#" + $(this).attr('id')).data("token"),
    //        nav: $("#" + $(this).attr('id')).data("nav"),
    //        navchange: $("#" + $(this).attr('id')).data("navchange"),
    //        navchangeper: $("#" + $(this).attr('id')).data("navchangeper"),
    //        navdate: $("#" + $(this).attr('id')).data("navdate"),
    //        formtitle: "Lumpsum",
    //        txnType: "FP"
    //    };
    //    $.post("/MutualFund/LUMPSUMForm", { sip_lumpsum_order: siplumpsumorder }, function (response) {
    //        var orderformname = "OrderFormMutualFundLumpsum_" + randomNum
    //        $("#lumpsumform").html(response);
    //        $("#" + orderformname).modal("show");
    //        $("#dvLoader").hide();
    //    });
    //});

    function ShowQuote(isin, schemecode, fundtype, schemename) {
        //try {
        //    // Particular event function for netcore integration - Vishal
        //    smartech('dispatch', 'MF_GetQuote', {
        //        'scheme_name': schemename,
        //        'redirection_source': 'Home'
        //    });
        //}
        //catch (err) {
        //    console.log('Smarttech not initiated in MF_GetQuote');
        //    createNetcoreLog('MF_GetQuote');

        try {
            clevertap.event.push('Web_MF_Quote', {
                'scheme_name': schemename,
                "Date": new Date()
            });
        }
        catch {
            createNetcoreLog('Web_MF_Quote');
        }

        

        $("#dvLoader").show();
        var url = "/Home/GetQuoteMFPage";
        var token = $('[name=__RequestVerificationToken]').val();
        var data = EncryptData(('{schemeCode:"' + schemecode + '",isin:"' + isin + '",divFlag:"' + fundtype + '"}'));

        $.ajax({
            type: "POST",
            url: url,
            data: JSON.stringify(data),
            headers: { '__RequestVerificationToken': token },
            contentType: 'application/json; charset=utf-8',
            //data: {
            //    'schemeCode': schemecode,
            //    'isin': isin,
            //    'divFlag': fundtype
            //},
            async: true,
            success: function (html) {
                $("#dvLoader").hide();
                VerifyJSON(html);
            },
            error: function (html) {
                $("#dvLoader").hide();
                alert('Error');
            }
        });
    }

    $(".showMFQuote").click(function () {
        
        $("#dvLoader").show();
        var isin = $("#" + $(this).attr('id')).data("mainisin");
        var schemecode = $("#" + $(this).attr('id')).data("mainschemecode");
        var fundtype = $("#" + $(this).attr('id')).data("mainfundtype");
        var url = "/Home/GetQuoteMFPage";
        var token = $('[name=__RequestVerificationToken]').val();

        var data = EncryptData(('{schemeCode:"' + schemecode + '",isin:"' + isin + '",divFlag:"' + fundtype + '"}'));


        $.ajax({
            type: "POST",
            url: url,
            //data: {
            //    'schemeCode': schemecode,
            //    'isin': isin,
            //    'divFlag': fundtype
            //},
            data: JSON.stringify(data),
            headers: { '__RequestVerificationToken': token },
            contentType: 'application/json; charset=utf-8',
            async: true,
            success: function (html) {
                $("#dvLoader").hide();
                VerifyJSON(html);
            },
            error: function (html) {
                $("#dvLoader").hide();
                alert('Error');
            }
        });
    });



    //function MFCleverMFNFOordertrigger(tabname, schemename, schemetype, startdate, Eventname) {
    //    try {
    //        clevertap.event.push(Eventname, {
    //            "FundCategories": tabname,
    //            "TypeofFunds": schemename,
    //            "Segment": schemetype,
    //            "InvestmentType": startdate,
    //            "Date": new Date()

    //        });
    //    }
    //    catch {
    //        createNetcoreLog(EventName);
    //    }
    //}

    function MFWebMFordertrigger_Home(TypeofFunds, schemeName, schemeType, InvestmentType, SOURCENAME) {

        try {
            var fundtype = "";
            if (TypeofFunds == "10") {
                fundtype = "Index Funds";
            }
            if (TypeofFunds == "1") {
                fundtype = "High Returns";
            }
            if (TypeofFunds == "2") {
                fundtype = "Top Rated Funds";
            }
            if (TypeofFunds == "3") {
                fundtype = "Equity Funds";
            }
            if (TypeofFunds == "4") {
                fundtype = "Tax Saver Funds";
            }
            if (TypeofFunds == "5") {
                fundtype = "Better Than FD's";
            }
            if (TypeofFunds == "6") {
                fundtype = "Top Hybrid Funds";
            }
            if (TypeofFunds == "") {
                fundtype = "Index Funds";
            }

            if (SOURCENAME == "") {
                SOURCENAME = "Mutual Fund Page/Home Page";
            }
            
            clevertap.event.push('Web_MF_order_trigger', {
                "Source": SOURCENAME,
                "MF Name": schemeName,
                "Fund Categories": "Theme-Based MF",
                "Type of Funds": fundtype,
                "Segment": schemeType,
                "Investment Type": InvestmentType,
                "Date": new Date()
            });
        }
        catch {
            createNetcoreLog('Web_MF_order_trigger')
        }
    }
