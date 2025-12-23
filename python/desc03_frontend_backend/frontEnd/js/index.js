

// 제품
function pBtnClickEvent() {
    $('#p_btn').on('click', function () {
        var p_nameVal = $('#p_name').val()
        var p_priceVal = $('#p_price').val()
        var p_stockVal = $('#p_stock').val()

        $.ajax({
            url: "http://127.0.0.1:8000/product.reg",
            data: { "p_name": p_nameVal, "p_price": p_priceVal, "p_stock": p_stockVal },
            beforeSend: function (req) {
                // req.setRequestHeader("Authorization", "KakaoAK 4728978749201b35c97c6c303ce804b4");
            },
            success: function (regResult) {
                alert(regResult.result)
                getProduct()
            },
            error: function (request, status, error) {

            }
        })
    })
}

// 판매자
function uBtnClickEvent() {
    $('#s_btn').on('click', function () {
        var s_nameVal = $('#s_name').val()
        var s_birthdayVal = $('#s_birthday').val()
        var s_addrVal = $('#s_addr').val()

        $.ajax({
            url: "http://127.0.0.1:8000/seller.reg",
            data: { "s_name": s_nameVal, "s_birthday": s_birthdayVal, "s_addr": s_addrVal },
            beforeSend: function (req) {
                // req.setRequestHeader("Authorization", "KakaoAK 4728978749201b35c97c6c303ce804b4");
            },
            success: function (regResult) {
                alert(regResult.result)
                getSeller(1)
            },
            error: function (request, status, error) {

            }
        })
        $('#s_name').val("")
        $('#s_birthday').val("")
        $('#s_addr').val("")
    })
}


function getSeller(p) {
    $.ajax({
        url: "http://127.0.0.1:8000/seller.get",
        data: { "page": p },
        success: function (sellerResult) {
            $('#s_bbs').empty()
            $(sellerResult.sellers).each(function (i, r) {
                var no = r.no
                var name = r.name
                var bd = r.bd
                var addr = r.addr
                $("#s_bbs ").append('<li>' + '<a href="#sellerDetailPage" onclick="getSellerDetail(' + no + ')">' + name + '<br>' + bd + '<br>' + addr + '</li>')
            })
            $('#s_bbs').listview('refresh')

            $("#sellerPageControlTbl td").empty();
            for (var i = 1; i <= sellerResult.pageCount; i++) {
                var a = $('<a></a>').attr('onclick', 'getSeller(' + i + ');').text(i)
                $('#sellerPageControlTbl td').append(a)
            }
        },
        error: function (request, status, error) {

        }
    })
}


function getSellerDetail(no) {
    $.ajax({
        url: "http://127.0.0.1:8000/seller.get.detail",
        data: { "no": no },
        success: function (sellerResult) {
            $("#sellerNo").val(sellerResult.no)
            $("#sellerName").val(sellerResult.name)
            $("#sellerBirthday").val(sellerResult.bd)
            $("#sellerAddr").val(sellerResult.addr)
        }
    })
}

function getProduct(p) {
    $.ajax({
        url: "http://127.0.0.1:8000/product.get",
        data: { 'page': p },
        success: function (productResult) {

            $('#p_bbs').empty()
            $(productResult.products).each(function (i, r) {
                var name = r.name
                var price = r.price
                var stock = r.stock
                $("#p_bbs ").append('<li>' + name + '<br>' + price + '<br>' + stock + '</li>')
            })
            $('#p_bbs').listview('refresh')
            $("#productPageControlTbl td").empty();
            for (var i = 1; i <= productResult.pageCount; i++) {
                var a = $('<a></a>').attr('onclick', 'getProduct(' + i + ');').text(i)
                $('#productPageControlTbl td').append(a)

            }
        },
        error: function (request, status, error) {

        }
    })

}

function sellerUpdateBtn() {
    $('#sellerUpdateBtn').click(function () {
        var no = $('#sellerNo').val()
        var name = $('#sellerName').val()
        var addr = $('#sellerAddr').val()
        console.log(no, name, addr);
        $.ajax({
            url: "http://127.0.0.1:8000/seller.update",
            data: { 'no': no, 'name': name, 'addr': addr },
            success: function (sellerResult) {
                alert(sellerResult.result)
                $('#goSellerPageA').click()

            },
            error: function (request, status, error) {

            }
        })
    })
}

function sellerDeletebtn() {
    $('#sellerUDeleteBtn').click(function () {  
        var no = $('#sellerNo').val()
        if(confirm("진짜삭제?")){
        $.ajax({
            url: "http://127.0.0.1:8000/seller.delete",
            data: { 'no': no },
            success: function (sellerResult) {
                alert(sellerResult.result)
                $('#goSellerPageA').click()

            },
            error: function (request, status, error) {

            }
        })
        }
    })
}

var product2BBSPage = false;
var product2BBSPageNo = 1;

function goSellerPageEvent() {
    $('#goSellerPageA').click(function () {
        getSeller(1)
        product2BBSPage = false;
    })
}

function goProductPageEvent() {
    $('#goProductPageA').click(function () {
        getProduct(1)
        product2BBSPage = false;
    })
}
function getProduct2() {
    $.ajax({
        url: "http://127.0.0.1:8000/product2.get",
        data: { "page": product2BBSPageNo },
        success: function (productResult) {
            if (product2BBSPageNo == 1) {
                $("#p_bbs2").empty();
            }
            $(productResult.products).each(function (i, r) {
                var name = r.name
                var price = r.price
                var stock = r.stock
                $("#p_bbs2 ").append('<li>' + name + '<br>' + price + '<br>' + stock + '</li>')
            })
            $('#p_bbs2').listview('refresh')
        },
        error: function (request, status, error) {
        }
    })
}

function goProductPageBEvent() {
    $("#goProductPageB").click(function () {
        product2BBSPage = true;
        product2BBSPageNo = 1
        getProduct2()
    })
}

function connectScrollEvent() {
    
    $(window).scroll(function () {
        var htmlHeight = $(document).height();  // 웹페이지 문서의 전체 높이
        var browserHeight = $(window).height();  //사용자가 지금보이는 브라우저 창의 높이
        var scrollTop = $(window).scrollTop(); // 스크롤바가 얼마나 내려왔는지, 맨 위라면 0임
        var scrollBottom = scrollTop + browserHeight; //현재 화면에서 가장 아랫부분의 위치  
 
        if (product2BBSPage && (scrollBottom >= htmlHeight - 10)) {//스크롤 아래값 >= 문서의 높이
            product2BBSPageNo++;
            getProduct2();
        }
    });
}
 
$(function () {
    goSellerPageEvent()
    goProductPageEvent()
    goProductPageBEvent()
    uBtnClickEvent()
    pBtnClickEvent()
    connectScrollEvent()
    sellerDeletebtn()
    sellerUpdateBtn()
 
})