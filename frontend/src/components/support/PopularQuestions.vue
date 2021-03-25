<template>
  <section class="uk-margin-xlarge-top">
    <div class="uk-container">
      <h2 class="uk-margin-medium-bottom">
        Most Popular Questions
        <a
          href="#"
          data-uk-totop
          data-uk-scroll
          class="uk-float-right uk-link uk-margin-small-top"
        ></a>
      </h2>
      <hr class="uk-margin-remove" />
      <ModernList :items="questions" />

      <ArticleComponent title="Text6" id="article-1">
        <p>Text7</p>
        <p>Text8</p>
      </ArticleComponent>

      <ArticleComponent title="Text9" id="article-2">
        <p>Text10</p>
      </ArticleComponent>

      <ArticleComponent title="Text11" id="article-3">
        <p>Text12</p>
      </ArticleComponent>

      <ArticleComponent title="Text13" id="article-4">
        <p>Text14</p>
      </ArticleComponent>

      <ArticleComponent title="Text15" id="article-5">
        <p>Text16</p>
      </ArticleComponent>

    </div>
  </section>
</template>

<script>
import ModernList from "./ModernList";
import ArticleComponent from "./ArticleComponent";

export default {
  name: "PopularQuestion",
  components: {
    ModernList,
    ArticleComponent
  },
  data() {
    return {
      questions: [
        { title: "Text1", ref: "#article-1" },
        { title: "Text2", ref: "#article-2" },
        { title: "Text3", ref: "#article-3" },
        { title: "Text4", ref: "#article-4" },
        { title: "Text5", ref: "#article-5" }
      ]
    };
  }
};
</script>