<template>
  <div
    class="uk-grid-medium uk-child-width-1-3@m uk-grid-small uk-grid-match tm-margin-large-top uk-text-center"
    data-uk-grid
    data-uk-scrollspy="cls: uk-animation-slide-bottom-medium; delay: 80"
  >
    <CategoryBox v-for="(item, i) in items" :key="i" :title="item.title" :icon="item.icon" :to="item.to" />
  </div>
</template>

<script>
import CategoryBox from "./CategoryBox";
export default {
  name: "Categories",
  components: {
    CategoryBox
  },
  data() {
    return {
      items: [
        { title: "Account and Profile", icon: "settings", to: "/settings" },
        { title: "Alias Login", icon: "heart", to: "/settings" },
        { title: "Tou.sh Links", icon: "lock", to: "/settings" },
        { title: "Reporting", icon: "home", to: "/settings" },
        { title: "Privacy and Security", icon: "cart", to: "/settings" },
        { title: "Bugs", icon: "check", to: '/settings' }
      ]
    };
  }
};
</script>