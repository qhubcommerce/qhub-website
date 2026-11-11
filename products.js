/* QHUB HERBAL — dữ liệu sản phẩm dùng chung cho trang chủ, trang thương hiệu và trang chi tiết */
window.QHUB_HERBAL = {
  priceOld: 140000,
  price: 105000,
  giftEvery: 2,
  pack: "30 gói × 3 g (tịnh 90 g)",
  brew: "1 túi lọc + 200 ml nước 95–100 °C, hãm 5 phút",
  galleryLabels: ["Hộp trà", "Combo mua 2 tặng 1", "Thành phần trong mỗi túi trà", "Lý do nên chọn", "Cách pha", "Cam kết của QHUB HERBAL"],
  products: [
    {
      id: "dhc", slug: "tra-ca-gai-diep-ha-chau.html",
      name: "Trà Cà Gai – Diệp Hạ Châu", short: "Cà Gai – Diệp Hạ Châu",
      tagline: "Thanh lọc từ bên trong.",
      color: "#0F5A33", tint: "#EEF6F0",
      ing: ["Cà gai leo 40%", "Diệp hạ châu 15%", "Xạ đen", "An xoa", "Giảo cổ lam", "Cỏ ngọt"],
      desc: "Cà gai leo, diệp hạ châu phối cùng xạ đen và giảo cổ lam. Hậu ngọt tự nhiên từ cỏ ngọt, hợp nhịp sống nhiều cuộc hẹn.",
      fit: "Người hay thức khuya, tiệc tùng, ăn nhiều đồ chiên nướng",
      tcb: "35/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Phụ nữ mang thai, cho con bú, trẻ em, người đang điều trị bệnh: hỏi ý kiến bác sĩ trước khi dùng."
    },
    {
      id: "nv", slug: "tra-nam-vuong.html",
      name: "Trà Nam Vương", short: "Nam Vương",
      tagline: "Phong thái nuôi dưỡng từ bên trong.",
      color: "#1C2F86", tint: "#EEF2FB",
      ing: ["Ba kích", "Nhục thung dung", "Nấm ngọc cẩu", "Kim tiền thảo", "Dứa dại", "Mú từn", "Cỏ ngọt"],
      desc: "Bảy vị thảo mộc phương Đông: ba kích, nhục thung dung, nấm ngọc cẩu cùng kim tiền thảo, dứa dại, mú từn. Món quà chăm sóc dành cho phái mạnh.",
      fit: "Nam giới bận rộn, hoặc làm quà biếu người thân",
      tcb: "24/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Không dùng cho trẻ em, phụ nữ mang thai hoặc cho con bú. Người có bệnh thận, bệnh mạn tính hay đang dùng thuốc: hỏi ý kiến bác sĩ."
    },
    {
      id: "xht", slug: "tra-xau-ho-tim-tam-sen.html",
      name: "Trà Xấu Hổ Tím – Tâm Sen", short: "Xấu Hổ Tím – Tâm Sen",
      tagline: "Để mỗi giấc ngủ là một lần tái tạo.",
      color: "#5A2B88", tint: "#F3EFFA",
      ing: ["Xấu hổ tím 30%", "Tâm sen 10%", "Lạc tiên", "Đinh lăng", "Hoa cúc vàng", "Cỏ ngọt"],
      desc: "Xấu hổ tím, tâm sen, lạc tiên cùng đinh lăng và hoa cúc vàng. Tách trà dịu hương cúc cho buổi tối thư thái.",
      fit: "Người muốn có thói quen thư giãn trước giờ nghỉ ngơi",
      tcb: "28/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Phụ nữ mang thai, cho con bú, trẻ em, người dị ứng họ Cúc hay đang dùng thuốc: hỏi ý kiến bác sĩ trước khi dùng."
    },
    {
      id: "ndv", slug: "tra-ngay-dau-ve.html",
      name: "Trà Ngày Dâu Về", short: "Ngày Dâu Về",
      tagline: "Thương em, thương đến mềm lòng.",
      color: "#A1162E", tint: "#FBE6EA",
      ing: ["Ích mẫu", "Mâm xôi", "Ngải cứu", "Cỏ máu", "Táo đỏ", "Gừng", "Cam thảo", "Thiên niên kiện"],
      desc: "Gừng, ngải cứu, táo đỏ — những vị tính ấm — cùng năm thảo mộc khác. Tách trà ấm cho những ngày đặc biệt của phái nữ.",
      fit: "Phái nữ, hoặc làm quà cho người mình thương",
      tcb: "32/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Không dùng khi có thai, nghi có thai hoặc cho con bú. Người tăng huyết áp, bệnh tim, gan, thận hay đang dùng thuốc: hỏi ý kiến bác sĩ."
    },
    {
      id: "loi", slug: "tra-la-oi-mix-la-sen.html",
      name: "Trà Lá Ổi Mix Lá Sen", short: "Lá Ổi Mix Lá Sen",
      tagline: "Cân bằng sau những bữa ngon.",
      color: "#5C7F1E", tint: "#EFF6DA",
      ing: ["Lá ổi 50%", "Lá sen 20%", "Giảo cổ lam", "Gạo lứt", "Cỏ ngọt"],
      desc: "Lá ổi, lá sen cùng giảo cổ lam và gạo lứt. Vị thanh mát, thơm hương ngũ cốc, dễ uống sau bữa ăn.",
      fit: "Người hay ăn tiệc, lẩu nướng, đồ nhiều dầu mỡ",
      tcb: "46/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Phụ nữ mang thai, cho con bú, trẻ em, người đang điều trị bệnh: hỏi ý kiến bác sĩ trước khi dùng."
    },
    {
      id: "dta", slug: "tra-duong-tam-an.html",
      name: "Trà Dưỡng Tâm An", short: "Dưỡng Tâm An",
      tagline: "Thân khỏe, tâm an, tuệ sáng.",
      color: "#8E2A5E", tint: "#FBE8F0",
      ing: ["Lạc tiên", "Tâm sen", "Đinh lăng", "Hoa cúc vàng"],
      desc: "Bốn vị tinh gọn: lạc tiên, tâm sen, đinh lăng, hoa cúc. Một khoảng nghỉ năm phút giữa ngày bận rộn.",
      fit: "Người làm việc nhiều với màn hình, lịch kín cả ngày",
      tcb: "36/ANH KHOI/2026",
      note: "Không dùng cho người mẫn cảm với bất kỳ thành phần nào. Phụ nữ mang thai, cho con bú, trẻ em, người dị ứng họ Cúc hay đang dùng thuốc: hỏi ý kiến bác sĩ trước khi dùng."
    }
  ]
};

window.QHUB_CONTACT = {
  phone: "0856510113",
  phoneText: "0856 510 113",
  email: "qhubcommerce@gmail.com",
  formEndpoint: "https://formsubmit.co/ajax/qhubcommerce@gmail.com"
};
