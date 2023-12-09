### [Scene Representation Transformer](https://arxiv.org/pdf/2111.13152.pdf)
- Summary: End to end CNN + transformer + light field/volume query
- Arch: Images+Pose(optional)+Camera->CNN->Encoder Transformer->latent set encoding->decoder
![](/images/srt-1.png)
- Ablations: Without pose input or using volume rendering achieves comparable results
- Results: ![](/images/srt-2.png)