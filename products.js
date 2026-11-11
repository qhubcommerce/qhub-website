/* QHUB HERBAL — dữ liệu sản phẩm. Sửa giá / mô tả tại đây. */
window.QHUB_HERBAL = {
  priceOld: 160000,
  price: 105000,
  // Mua 2 tặng 1: cứ 2 hộp mua được tặng thêm 1 hộp
  giftEvery: 2,
  products: [
    { id: "dhc", name: "Trà Cà Gai Diệp Hạ Châu", ing: "Cà gai leo · Diệp hạ châu",
      desc: "Vị thảo mộc thanh, hậu ngọt nhẹ. Túi lọc tiện pha, hợp uống hằng ngày sau bữa ăn.",
      img: "p-dhc.jpg", img2: "p-dhc-2.jpg" },
    { id: "nv", name: "Trà Nam Vương", ing: "Phối trộn thảo mộc Nam",
      desc: "Hương thảo mộc đậm, ấm. Pha nóng hoặc ủ lạnh đều ngon.",
      img: "p-nv.jpg", img2: "p-nv-2.jpg" },
    { id: "xht", name: "Trà Xấu Hổ Tím Tâm Sen", ing: "Xấu hổ tím · Tâm sen",
      desc: "Vị dịu, thơm mùi sen. Hợp cho tách trà buổi tối, thư giãn cuối ngày.",
      img: "p-xht.jpg", img2: "p-xht-2.jpg" },
    { id: "ndv", name: "Trà Ngày Dâu Về", ing: "Phối trộn thảo mộc",
      desc: "Vị nhẹ, dễ uống, hương thơm dịu. Món quà ý nghĩa cho người thân.",
      img: "p-ndv.jpg", img2: "p-ndv-2.jpg" },
    { id: "loi", name: "Trà Lá Ổi Mix Lá Sen", ing: "Lá ổi · Lá sen",
      desc: "Vị chát nhẹ, thanh mát. Hợp với người thích trà ít ngọt, uống thay nước.",
      img: "p-loi.jpg", img2: "p-loi-2.jpg" },
    { id: "dta", name: "Trà Dưỡng Tâm An", ing: "Phối trộn thảo mộc",
      desc: "Vị êm, hương thảo mộc dịu. Dành cho những phút chậm lại trong ngày.",
      img: "p-dta.jpg", img2: "p-dta-2.jpg" }
  ]
};
window.QHUB_CONTACT = {
  phone: "0856510113",
  phoneText: "0856 510 113",
  email: "qhubcommerce@gmail.com",
  // Form gửi về email qua FormSubmit (lần đầu cần bấm link kích hoạt trong email)
  formEndpoint: "https://formsubmit.co/ajax/qhubcommerce@gmail.com"
};
